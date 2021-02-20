from newsapi import NewsApiClient
import TextToSpeech
import os
from dotenv import load_dotenv
load_dotenv()
import eel

newsapi = NewsApiClient(api_key=os.getenv('NEWS_APY'))


def getNews(query):

    all_articles = newsapi.get_everything(q=query, language='en', page_size=5, sort_by='relevancy')
    if str(all_articles['status']) == 'ok':
        data = all_articles['articles']
        f = open("news.txt", "w")
        for x, y in enumerate(data):
            f.write(f'\nTitle:- {y["title"]} \nURL:- {y["url"]}\nContent:- {y["content"]}\n')
        f.close()
        eel.printAgentDom("Your Top 5 result for your query is stored in news.txt")
        TextToSpeech.say("Your Top 5 result for your query is stored in news.txt")
    else:
        eel.printAgentDom("Sorry I Didn't Get the Result")
        TextToSpeech.say("Sorry I Didn't Get the Result")


