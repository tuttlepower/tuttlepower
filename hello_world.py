# import libraries
import tweepy
import os

# Retreive secrets
CONSUMER_KEY = os.environ.get['CONSUMER_KEY']
CONSUMER_SECRET = os.environ.get['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ.get['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ.get['ACCESS_TOKEN_SECRET']

print(CONSUMER_KEY)
