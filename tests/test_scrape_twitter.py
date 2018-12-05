from tweego.scrape_twitter import StreamListener
from tweego import scrape_twitter


def test_get_media(tweet):
    sl = StreamListener(1,None)
    media_url, media_type = sl.get_media(tweet)
    assert media_url == None
    assert media_type == ''

def test_get_hashtags(tweet):
    sl = StreamListener(1,None)
    hashtags = sl.get_hashtags(tweet)
    assert 'data science' in hashtags

def test_get_tweet_dict(tweet):
    sl = StreamListener(1,None)
    tweet = sl.get_tweet_dict(tweet)
    assert tweet['text'] == 'What To Expect For AI (Artificial Intelligence) In 2019'


result = []

def callback(tweet):
    result.append(tweet)

def test_get_tweets():
    """Connection to Twitter is established"""
    scrape_twitter.get_tweets(3, callback)
    print(result)
    assert result[0]["username"] != ""
