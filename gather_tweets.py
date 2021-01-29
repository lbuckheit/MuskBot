import tweepy
import configparser

config = configparser.ConfigParser()
config.read('./secrets/config.ini')
twitter = config['twitter']
auth = tweepy.OAuthHandler(twitter['api_key'], twitter['secret_key'])
auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
api = tweepy.API(auth)

tweets = []

for tweet in api.user_timeline('elonmusk', tweet_mode="extended"):
  tweets.append(tweet.full_text)

for tweet in api.user_timeline('stoolpresidente', tweet_mode="extended"):
  tweets.append(tweet.full_text)

for tweet in api.user_timeline('chamath', tweet_mode="extended"):
  tweets.append(tweet.full_text)

with open('test_tweets.txt', 'w', encoding="utf-8") as f:
  for tweet in tweets:
    f.write(tweet + '\n')