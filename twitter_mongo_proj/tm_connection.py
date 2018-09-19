#import argparse
import urllib
import pymongo
from load_mongo import load_data
from scrape_twitter import get_tweets

username = ""
password = ""
username = ''#urllib.parse.quote_plus(username)
password = ''#urllib.parse.quote_plus(password)
#MONGO_HOST = pymongo.MongoClient()
#f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites = true"

class read_into_Mongo:
    def __init__(self,chunk_size,db,limit):
        self.chunk_size = chunk_size
        self.db = db
        self.buffer = []
        self.limit = limit
        self.counter = 0
    def new_tweet(self, text):
        #db = MONGO_HOST
        self.buffer.append(text)
        if self.limit - self.counter < self.chunk_size:
            self.chunk_size = self.limit - self.counter
        if len(self.buffer) >= self.chunk_size:
            load_data(self.db,self.buffer)
            self.buffer = []
            self.counter += self.chunk_size
        print("Processed Tweet")


def load_to_mongo(chunk_size,db,limit):
    get_tweets(limit,read_into_Mongo(chunk_size,db,limit).new_tweet)

if __name__=='__main__':
    load_to_mongo(50,pymongo.MongoClient(),1500)
    