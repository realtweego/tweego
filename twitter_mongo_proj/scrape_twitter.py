import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()
print("connection established with user: ", user.name)
DEFAULT_HASHTAGS = ['Machine learning', '#ML',
                    'BigData', 'Artificial Intelligence', 'Big Data']


class StreamListener(tweepy.StreamListener):
    def __init__(self, limit, callback):
        super().__init__()
        self.limit = limit
        self.counter = 0
        self.callback = callback

    def on_error(self, status_code):
        '''stops stream when error 420 occurs'''
        if status_code == 420:
            return False

    def on_data(self, data):
        '''collect, filter and parse the tweets from twitter API'''
        t = json.loads(data)
        created_at = t['created_at']
        tweet_id = t['id_str']
        if 'extended_tweet' in t:
            text = t['extended_tweet']['full_text']
        else:
            text = t['text']
        username = t['user']['screen_name']
        followers_count = t['user']['followers_count']
        user_favorites_count = t['user']['favourites_count']
        retweet_count = t['retweet_count']
        favorite_count = t['favorite_count']
        hashtags = []
        if 'extended_tweet' in t:
            for hashtag in t['extended_tweet']['entities']['hashtags']:
                hashtags.append(hashtag['text'])
        elif 'hashtags' in t['entities'] and len(t['entities']['hashtags']) > 0:
            hashtags = [item['text'] for item in t['entities']['hashtags']]
        else:
            hashtags = []

        media_url = []
        if 'extended_tweet' in t and 'media' in t['extended_tweet']['entities']:
            for media in t['extended_tweet']['entities']['media']:
                media_url.append(media['media_url_https'])
                media_type = media['type']
        else:
            media_url = None
            media_type = ''

        if t['retweeted'] == False and 'RT' not in t['text'] and t['in_reply_to_status_id'] == None:
            tweet = {'created_at': created_at, 'id': tweet_id,
                     'text': text, 'username': username,
                     'followers': followers_count,
                     'user_favorites_count': user_favorites_count,
                     'retweets': retweet_count, 'favorites': favorite_count,
                     'hashtags': hashtags, 'media_url': media_url,
                     'media_type': media_type, 'interesting': 0}
            self.callback(tweet)
            self.counter += 1
            if self.counter == self.limit:
                return False


def get_tweets(limit, callback):
    stream_listener = StreamListener(limit, callback)
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=DEFAULT_HASHTAGS, languages=['en'])


if __name__ == '__main__':
    get_tweets(5, print)
