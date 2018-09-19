'''Feature to push messages to twitter'''
#http://nodotcom.org/python-twitter-tutorial.html

import tweepy
import os
import pymongo
import urllib
import pandas as pd

#Create function for the API configration to use twitter
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

# Configuration of the Twitter access using access credentials.
def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : ""
    "consumer_secret"     : ""
    "access_token"        : ""
    "access_token_secret" : "" 
    }

  #Set up API
  api = get_api(cfg)
  # Create tweet and send it to twitter
  tweet = a
  status = api.update_status(status=tweet)
  
#%run -i environ_vars
username = ""
password = ""
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")

db = client.twitter # client.twitter_test
posts = db.collections.tweets_labeled
df = posts.find()
df = pd.DataFrame(list(df))
df.head()

df.iloc[df[df["followers"] == df["followers"].max()].index[0]]["text"]

if __name__ == "__main__":
  main()