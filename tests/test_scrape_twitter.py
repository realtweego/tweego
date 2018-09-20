from tweego.scrape_twitter import StreamListener
import json

t = json.loads(open('samples.json').read())

def test_get_media(t):
	media_url, media_type = get_media(t)
	assert media_url == 'http://pbs.twimg.com/media/DnhXeb7UYAEdKrQ.jpg'
	assert media_type == 'photo'

def test_get_hashtags(t):
	hashtags = get_hashtags(t)
	assert hashtags == ['DataScience', 'MachineLearning','BigData']

def test_get_tweet_dict(t):
	tweet = get_tweet_dict(t)
	assert tweet['text'] == 'RT @IainLJBrown: Examining The Positive And Negative Impacts of AI On Education #DataScience #MachineLearning #DeepLearning #NLP #Robots #A…'
