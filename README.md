<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="780" height="520">
  </a>
  <h3 align="center">FINS</h3>
  <p align="center">
FINS (Financial News Summarizer) is a system that intakes financial news articles and simplifies the article into a quick and easy to read summary.
<br />
        <p align='center'>Illustration by <a href="https://www.freepik.com/vectors/computer">from Freepik</a></p>
</p>
<br />

<!-- ABOUT THE PROJECT -->

## About The Project
FINS (Finacial News Summarizer) uses a combination of webscraping, extractive summarization and Flask-RESTful to create a simple api that summarizes financial news articles.  Extractive summarization works by assigning weights to the sentences through a series of tokenization.  This program is built to create summaries by only using sentences with a weighted score above three standard deviations from the mean weight, capturing only the most important content.

While this program can be used to summarize any text, it is specifically set up to scrape financial news from  reuters, cnbc, yahoo finance and marketwatch. The program targets a unique class for each news source to ensure that it is grabbing only the article text.  If a url outside of these sources is passed, the program will default to grabbing all of the paragraph tags in the article.  To start the API, simply run the api.py file and pass an encoded article url after the /fins/? route.  The api root page response has examples on how encode the url.  

### Built With

- nltk
- flask
- flask-restful
- bs4

<!-- GETTING STARTED -->

## Getting Started

To get started, clone this repo, cd into the root directory and run ```pip install -r requirements.txt```.  Then simply run ```flask run``` or ```python3 app.py``` to start the api.  Once the server is active, you can send a get request to /fins/? with an encoded url to get the article summary.  Check out example.py to see a get request to the server in action!