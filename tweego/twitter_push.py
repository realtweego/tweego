from math import ceil
import tweepy
import pymongo
from tweego.tm_connection import load_to_mongo
from tweego.config import cfg, client
from math import ceil


#Create function for the API configration to use twitter
def get_api():
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main(chunk_size, limit):
    api = get_api()
    # Create tweet and send it to twitter
    load_to_mongo(chunk_size, limit)
    streamed = list(client.twitter.collections.tweets_labeled.find({'interesting':1}).\
                    sort('$natural', pymongo.DESCENDING).limit(ceil(int(f'{limit}')/int(f'{chunk_size}'))))
    followers = [tw['followers'] for tw in streamed]
    for tweet in streamed:
        if tweet['followers'] == max(followers):
            message = 'By @'+tweet['username']+'\n\n'+tweet['text']
    return api.update_status(status=message)

if __name__ == "__main__":
    main(3, 10)
