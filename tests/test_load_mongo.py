from tweego.tm_connection import read_into_Mongo
from tweego.tm_connection import load_to_mongo
from tweego.config import client
import json
def test_load_mongo(tweet):

	rim = read_into_Mongo(1,1)
	before = client.twitter.collections.tweets_labeled.count()
	tweet = json.loads(tweet)
	rim.new_tweet(tweet)
	load_to_mongo(1,1)
	after = client.twitter.collections.tweets_labeled.count()
	assert after > before 

 
