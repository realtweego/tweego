#import argparse
import pymongo
#import urllib
import json

from scrape_twitter import get_tweets
from load_mongo import load_data


#1) Define Database
MONGO_HOST = 'mongodb://localhost/twitter.db'

"""
# This code establishes the connection to the MongoDB Cloud Server
%run -i environ_vars

username = os.environ.get("MONGODB_USERNAME", '')
password = os.environ.get("MONGODB_PASSWORD", '')
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")
"""
def run():
    ''' This function uses scrape_twitter.py to access Twitter and retrieve tweets through
        tweepy. It than opens an MongoDB and stores the tweets'''

    #2) Get tweets based on generator
    get_tweets()

    #2.2) Open tweets-file and store all tweets in a list
    with open('tweets.json') as data:
        data_list = []
        for i in data:
            data_list.append(json.loads(i))

    #3) Open Database and store tweets in MongoDB from a JSON-file in current working directory
    load_data(MONGO_HOST, data_list)

if __name__ == "__main__":
    run()
