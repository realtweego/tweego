#import argparse
import pymongo
import urllib
import json
from scrape_twitter import get_tweets
from load_mongo import load_data
from scrape_twitter import get_tweets
#from pymongo import MongoClient

username = ""
password = ""
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
MONGO_HOST = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")


class read_into_Mongo:
    def __init__(self,chunk_size,db):
        self.chunk_size = chunk_size
        self.db = db
        self.buffer = []

    def new_tweet(self, text):
        #db = MONGO_HOST
        self.buffer.append(text)
        if len(self.buffer) >= self.chunk_size:
            load_data(self.db,self.buffer)
            self.buffer = []
        print("Processed Tweet")


m = read_into_Mongo(3,MONGO_HOST)


# figure out a smarter way to specify this
get_tweets(9,m.new_tweet)