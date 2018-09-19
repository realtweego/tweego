'''Feature to push messages to twitter'''
#http://nodotcom.org/python-twitter-tutorial.html

import tweepy
import os
import pymongo
import urllib
import pandas as pd
from tm_connection import load_to_mongo

username = ""
password = ""
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")

#Create function for the API configration to use twitter
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

# Configuration of the Twitter access using access credentials.
def main(chunk_size,limit):
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  #Set up API
  api = get_api(cfg)
  # Create tweet and send it to twitter
  load_to_mongo(chunk_size,limit,client)
  streamed=list(client.twitter.collections.tweets_labeled.find({'interesting':1}).sort('$natural',pymongo.DESCENDING).limit(int(f'{limit}')))
  followers=[]
  for t in streamed:
      followers.append(t['followers'])
  for t in streamed:
      if t['followers']==max(followers):
          tweet= 'By @'+t['username']+'\n\n'+t['text']
  #tweet = list(client.twitter.collections.tweets_labeled.find({'interesting':1}).sort([('followers',pymongo.DESCENDING),('created_at',pymongo.DESCENDING)]).limit(int(f'{limit}')))[0]['text']
  status = api.update_status(status=tweet)
  
#%run -i environ_vars
#username = "basil_master"
#password = "basil_spice"
#username = urllib.parse.quote_plus(username)
#password = urllib.parse.quote_plus(password)
#client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")

#db = client.twitter # client.twitter_test
#posts = db.collections.tweets_labeled


if __name__ == "__main__":
  main(3,10)