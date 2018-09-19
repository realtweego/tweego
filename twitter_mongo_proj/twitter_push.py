
'''Feature to push messages to twitter'''
#http://nodotcom.org/python-twitter-tutorial.html

#Import necessary packages
import tweepy

#Create function for the API configration to use twitter
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

# Configuration of the Twitter access using access credentials.
def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }
  #Set up API
  api = get_api(cfg)
  # Create tweet and send it to twitter
  tweet = "Hi I am the SPICED - Machine Learning BOT. This is my first tweet. Let the learning begin! #AI#MachineLearning#DeeperDeepLearning"
  status = api.update_status(status=tweet)

if __name__ == "__main__":
  main()