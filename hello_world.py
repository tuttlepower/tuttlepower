# import libraries
import tweepy
import os

#sets up the api to play with Twitter
def py_twit_setup():
  # Retreive secrets
  CONSUMER_KEY = os.environ['CONSUMER_KEY']
  CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
  ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
  ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
  # passes unique identification into an authorization to use tweepy
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  # returns the auth to automatically plug into tweepy and set api
  return auth

# uses unique auth to set up API access 
api = tweepy.API(py_twit_setup())
print('Success')
