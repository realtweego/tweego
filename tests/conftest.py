
import pytest
import json
from unittest.mock import MagicMock
import pymongo
import tweepy

#
# Mocking so that tests run without credentials
#
pymongo.MongoClient = MagicMock()
tweepy.StreamListener.stream = MagicMock()
tweepy.OAuthHandler = MagicMock()
tweepy.API = MagicMock()

def send_tweet(self, *args, **kwargs):
    """Stub for filter method that returns one single tweet"""
    self.listener.on_data(open('tweet.json').read())

tweepy.Stream.filter = send_tweet

@pytest.fixture
def tweet():
    s = open('tweet.json').read()
    j = json.loads(s)
    return j

@pytest.fixture
def parsed_tweet():
    s = open('parsed_tweet.json').read()
    j = json.loads(s)
    return j
