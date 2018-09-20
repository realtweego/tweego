import argparse
import pymongo
from scrape_twitter import get_tweets
from config import client


class read_into_Mongo:

    def __init__(self, chunk_size, limit):
        self.chunk_size = chunk_size
        #self.db = client
        self.buffer = []
        self.limit = limit
        self.counter = 0
    def load_data(self):
        '''insert the data into the mongoDB into a collection called tweets
        if tweets doesn't exist, it will be created.'''

        followers = [tweet['followers'] for tweet in self.buffer]
        for tweet in self.buffer:
            if tweet['followers'] == max(followers):
                tweet['interesting'] = 1
        client.twitter.collections.tweets_labeled.insert(self.buffer)

    def new_tweet(self, text):
        self.buffer.append(text)
        if self.limit - self.counter < self.chunk_size:
            self.chunk_size = self.limit - self.counter
        if len(self.buffer) >= self.chunk_size:
            self.load_data()
            self.buffer = []
            self.counter += self.chunk_size

def load_to_mongo(chunk_size, limit):
    get_tweets(limit, read_into_Mongo(chunk_size, limit).new_tweet)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Collect tweets and put them into a database')

    parser.add_argument('--chunk_size', type = int, default = 2, help = 'How many tweets do you want to grab at a time?')
    parser.add_argument('--client', type = str,default = "", help = 'Enter the string that points to the relevant database')
    parser.add_argument('--total_number', type=int, default = 4, help = 'How many total tweets do you want to get?')


    args = parser.parse_args()
    if args.client == "":
        client = pymongo.MongoClient()
    else:
        client = pymongo.MongoClient(args.client)

    load_to_mongo(args.chunk_size, args.total_number, client)