from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse
from summarize import get_summary, init_summarizer
from urllib.parse import urlencode, quote_plus, parse_qs


parser = reqparse.RequestParser()
parser.add_argument('article_url', type=str, help='Please pass an encoded article url')

#initialize the Flask app and Api
app = Flask(__name__)
api = Api(app)

# #class that handles the news article urls and returns the summary
class Fins(Resource):
    def __init__(self):
        self.__article_url=parser.parse_args().get('article_url',None)
    def get(self):
        try:
            if self.__article_url !=None:
                return{"response":200, 'summary': get_summary(url=self.__article_url)}
            else:
                return{'response':400, 'help':'make sure to enter an encoded article_url.  Go to / to see an example.'}
        except:
            return{'response':400, 'help':'make sure to enter an encoded article_url.  Go to / to see an example.'}


        # "{'summary': get_summary(url=parse_qs(qs=article)['article_url'][0])}"

class Homepage(Resource):
    init_summarizer()
    def get(self):
        return {'welcome': 'Enter an encoded article url after /fins/? to return the summary. See encoding_syntax for a help encoding the url and encoded_url_example to see an example of an encoded url', "encoding_syntax": "urlencode({'article_url':'https://www.reuters.com/business/wall-st-opens-higher-led-by-tech-shares-2021-05-13/'}, quote_via=quote_plus)",
        'encoded_url_example':urlencode({'article_url':'https://www.reuters.com/business/wall-st-opens-higher-led-by-tech-shares-2021-05-13/'}, quote_via=quote_plus)}


# #assign class to route
api.add_resource(Homepage, '/')
api.add_resource(Fins, '/fins/')



#run the app on start
if __name__ == '__main__':
    app.run(debug=True)
        