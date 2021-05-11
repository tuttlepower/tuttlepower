# import libraries
import tweepy
import os

# Tweets I don't want to delete
saved = [325340292708454401,
237388707492159488,
210417854527442944,
325017236454662144,
261203181093130240,
320662633667764225,
375766342927806464,
344316028853055489,
256580152413257729,
266016650720055296,
1228844600737091592,
1193635438168334336,
381566733183504384,
381567188609400832,
323504359658897408,
1216743103702405122,
1222634626142785536,
1226020550042103808,
1214349555652874240,
1235254227196248064,
1258484423953199104,
1248795234483519490,
1248796146925015040,
1248796258292113409,
1248796997919834113,
1259877525704015872,
1259855407117479936,
1259869039377223680,
1259869039377223680,
1259869039377223680,
1259869039377223680,
1252350302457434113,
1243223004512911365,
1246847450935164929,
1240401016752934914,
1176871140310077440,
1176901230104338434,
1176901997217427456,
1179086154706178050,
1199517471029563392,
1252347514755231746,
1323032182584213505,
1342194558134841345,
256580152413257729
]

print(len(saved))

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
  print('Auth')
  return auth

# uses unique auth to set up API access 
api = tweepy.API(py_twit_setup())

# Deletes an individual tweet
def tweet_delete(x):
  try:
    api.destroy_status(str(x))
  except:
    print('roll with the punches')

# Get Tweets I want to delete
def tweets_to_delete():
  tweet_list = []
  tweets = tweepy.Cursor(api.user_timeline,id='TuttlePower').items()
  for tweet in tweets:
    if tweet.favorite_count<=5 and tweet.id not in saved:
      tweet_list.append(tweet)
  print(len(tweet_list))
  return tweet_list

print('Calling tweets to delete')
try: 
  tweets = tweets_to_delete()
  print(len(tweets))

except:
  print('Job failed, Action Complete')

# for tweet in to_delete:
#   tweet_delete(tweet.id)
