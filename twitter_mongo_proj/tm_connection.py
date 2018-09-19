#import argparse
import pymongo
import urllib
import json


from scrape_twitter import get_tweets
import argparse
import sys


username = ""
password = ""
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
#MONGO_HOST = pymongo.MongoClient()
#f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true"

class read_into_Mongo:
    def __init__(self,chunk_size,db,limit):
        self.chunk_size = chunk_size
        self.db = db
        self.buffer = []
        self.limit=limit
        self.counter=0
    def load_data(self,client, data_list):
        #client = MONGO_HOST
        client = self.db
        #insert the data into the mongoDB into a collection called tweets
        #if tweets doesn't exist, it will be created.
        followers=[]
        for tweet in data_list:
            followers.append(tweet['followers'])
        #for i in range(len(data_list)//10):
        for tweet in data_list:
            if tweet['followers']==max(followers):
                tweet['interesting']=1
            #followers.remove(max(followers))
        client.twitter.collections.tweets_labeled.insert(data_list)

        #client.twitter.collections.tweets.insert(data_list)
    def new_tweet(self, text):
        #db = MONGO_HOST
        self.buffer.append(text)
        if self.limit - self.counter < self.chunk_size:
            self.chunk_size = self.limit - self.counter
        if len(self.buffer) >= self.chunk_size:
            self.load_data(self.db,self.buffer)
            self.buffer = []
            self.counter+=self.chunk_size
        print("Processed Tweet")


def load_to_mongo(chunk_size,limit,db):
    get_tweets(limit,read_into_Mongo(chunk_size,db,limit).new_tweet)

if __name__=='__main__':
    """
    Enter the function, and then
    """

    parser = argparse.ArgumentParser(description='Run NMF.')

    parser.add_argument('--chunk_size', type=int, default=2, help='How many tweets do you want to grab at a time?')
    parser.add_argument('--client', type=str,default="", help='Enter the string that points to the relevant database')
    parser.add_argument('--total_number', type=int, default=4, help='How many total tweets do you want to get?')


    args = parser.parse_args()
    if args.client=="":
        client = pymongo.MongoClient()
    else:
        client = pymongo.MongoClient(args.client)

    load_to_mongo(args.chunk_size,args.total_number,client)