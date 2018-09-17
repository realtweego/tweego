
import argparse

from import scrape_twitter
from load_mongo import on_data


def run_():
    ''' This function uses scrape_twitter.py to access Twitter and retrieve tweets through
        tweepy. It than opens an MongoDB and stores the tweets'''
    
    # (1) Connect to MongoDB instance
    client = MongoClient('mongodb://admin:Password1@localhost:27017/test')
    '''
    1. Get MongoDB details as required
    '''

    # (2)#Get tweets     
    twitter = scrape_twitter.()
    #functions I need to use    
    
    
    # (3) Store tweets in MongoDB
    load_mongo.on_data(twitter)
    #functions I need to use




if __name__ == "__main__":
    run()