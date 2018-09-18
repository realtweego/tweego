from load_mongo import on_data
from pymongo import MongoClient

def test_db_notempty():

	client = MongoClient()
	result = client.twitterdb.collections.count()
	assert result != 0


def test_on_data():

	client = MongoClient()
	before = client.twitterdb.collections.count()
	on_data()
	after = client.twitterdb.collections.count()
	assert after > before 

 
