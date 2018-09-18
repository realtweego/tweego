from load_mongo import load_data
from pymongo import MongoClient

def test_db_notempty():

	client = MongoClient()
	result = client.twitter.collections.tweets.count()
	assert result != 0


def test_load_mongo():

	client = MongoClient()
	before = client.twitter.collections.tweets.count()
	load_data()
	after = client.twitter.collections.tweets.count()
	assert after > before 

 
