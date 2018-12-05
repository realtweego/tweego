from tweego.tm_connection import read_into_Mongo
from tweego.tm_connection import load_to_mongo
from tweego.config import client


def test_load_mongo(parsed_tweet):
	rim = read_into_Mongo(1,1)
	rim.new_tweet(parsed_tweet)
	collection = client.twitter.collections.tweets_labeled
	assert collection.insert.called
