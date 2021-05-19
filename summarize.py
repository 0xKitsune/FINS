from requests import get
from re import sub
from bs4 import BeautifulSoup
from source_patterns import source_patterns
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import punkt
import nltk
import numpy as np
import re 

def init_summarizer():
    ##------------
    #uncomment if on mac, and ssl error when downloading stopwords/punkt
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    ##------------

    nltk.download('stopwords')
    nltk.download('punkt')


def get_summary(url=None, summary=None):   
    if url != None: 
        page = get(url=url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #identify the source to get the body of the text accurately 
        for source in source_patterns.keys():
            if source in url:
                paragraphs = soup.find("div", {"class":source_patterns[source]}).findAll('p')
            else:
                paragraphs = soup.find_all('p')
        # concat article paragrahs to one block of text
        article_text = ''
        for paragraph in paragraphs:
            article_text += paragraph.text + ' '
    elif summary !=None:
        article_text = summary

    # remove special characters, digits, extra spaces from original text
    article_text = sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = sub(r'\s+', ' ', article_text)
    # formatted article to create weights
    formatted_article_text = sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = sub(r'\s+', ' ', formatted_article_text)

    # tokenize article into sentences
    sentence_list = sent_tokenize(article_text)

    # create frequency for each word
    forbidden_words = stopwords.words('english')  

    word_frequencies = {}
    for word in word_tokenize(formatted_article_text):
        if word not in forbidden_words:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    #weighted frequency based on max weight
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max(word_frequencies.values())

    #calculate sentence scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
    
    #filter the most important sentences and join into one string
    summary_sentences = filter_most_important_sentences(sentence_scores=sentence_scores)
    summary = ''
    for sentence in summary_sentences:
        summary +=sentence + ' '
    
    #if the summary is longer than 5 sentences, call get_summary on the new summary to further refine the summary
    if len(re.findall("[A-Z].*?[\.!?]", summary, re.MULTILINE | re.DOTALL ))>5:
        print('reworking summary')
        summary = get_summary(summary=summary)

    return summary.replace("\\"," ")


def filter_most_important_sentences(sentence_scores):
    #getting threshold score based on standard deviation of weights to so the most important sentences are returned
    threshold_scores = []
    for value in sentence_scores.values():
        threshold_scores.append(value)      
    #using 3 std dev from the mean to get the most top .3% sentences in importance
    threshold = np.std(threshold_scores)*3

    #select the most important sentences
    summary_sentences = []
    for sentence in sentence_scores:
        if sentence_scores[sentence]> threshold:
            summary_sentences.append(sentence) 

    return summary_sentences

