import requests
from urllib.parse import urlencode, quote_plus



#to run this example, first run "flask run" or "python3 app.py"
#then once the server is up, you can call the api through a get request
#depending on the server you run flask on, you may need to change the server address below

def get_fins_summary(article_url, server_address='http://127.0.0.1:5000/'):
    #get the homepage to see the welcome message and help messages
    fins_homepage = requests.get(url=server_address).json()
    print(fins_homepage)

    #encode a dictionary that uses article_url as the key and the raw url as the value
    encoded_url=urlencode({'article_url':article_url}, quote_via=quote_plus)

    #send a get request to /fins? with the encoded url
    summary = requests.get(url='http://127.0.0.1:5000/fins?'+encoded_url).json()
    print(summary)

    return summary

#pass in an article url and get the summary
get_fins_summary(article_url='https://www.reuters.com/business/wall-st-opens-higher-led-by-tech-shares-2021-05-13/')

