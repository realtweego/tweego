# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:13:24 2018

@author: Mohamed Hammad
"""
import tweepy
import json
import sys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
user = api.me()
print (user.name)
counter=0
FILENAME = 'tweets.json'

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            return False
    
    def on_data(self, data):
        global counter
        t=json.loads(data)
        created_at=t['created_at']
        tweet_id=t['id_str']
        text = t['text']
        username = t['user']['screen_name']
        followers_count=t['user']['followers_count']
        user_favorites_count=t['user']['favourites_count']
        retweet_count=t['retweet_count']
        favorite_count=t['favorite_count']
        if 'retweeted_status' in t and len(t['retweeted_status']) > 0:
            hashtags=[item['text'] for item in t['retweeted_status']['entities']['hashtags']]
        else:
            hashtags=[]
        tweet = {'created_at':created_at,'id':tweet_id, 
                 'text':text, 'username':username, 
                 'followers':followers_count, 
                 'user_favorites_count':user_favorites_count, 
                 'retweets':retweet_count,'favorites':favorite_count,
                 'hashtags':hashtags}
        with open('tweets.json', 'a') as outfile:
                json.dump(tweet, outfile)
                outfile.write('\n')
                counter +=1
        if counter==100:
                sys.exit(0)

def get_tweets():
        stream_listener = StreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        stream.filter(track=['Machine learning','#ML','BigData','Artificial Intelligence','Big Data'], languages=['en'])#,async=True)

if __name__ == '__main__':
    get_tweets()