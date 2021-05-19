# To scrape only the article text and not other p-tag elements outside of the article (like text referring to other articles), specific sources are defined. 
# If not defined, it will search for all p-tags
source_patterns = {
'cnbc.com': 'group', 
'yahoo.com': 'caas-body',
'marketwatch.com':'article__body',
'reuters.com':'ArticleBody__container___D-h4BJ'
}
