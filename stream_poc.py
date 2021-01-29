# https://docs.tweepy.org/
# https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
# TODO - TRUECASING?
# TODO - FINE TUNE NE MODEL TO NOT CARE ABOUT CASE
# TODO - Model needs to not grab as many words like 'yeah' and 's'
# TODO - Slack integration (ping me, ability to immediately sell, etc.)
# TODO - Can probably auto strip out words he uses all the time like FSD and TESLA and LOOP
# TODO - Add: mike burry, the virgin galactic guy, portnoy

import tweepy
import configparser
import nltk
import sqlite3

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

def preprocess(sent):
  sent = nltk.word_tokenize(sent)
  sent = nltk.pos_tag(sent)
  sent = ne_chunk(sent)
  return sent

class MyStreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print(status.text)
    print('AAA')

  def on_error(self, status_code):
    print(status_code)
    if status_code == 420:
        #returning False in on_error disconects the stream
        return False

config = configparser.ConfigParser()
config.read('./secrets/config.ini')
twitter = config['twitter']
auth = tweepy.OAuthHandler(twitter['api_key'], twitter['secret_key'])
auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
api = tweepy.API(auth)

nes = []

# for tweet in api.user_timeline('cnbc'):
#   doc = nlp(tweet.text.lower())
#   for el in doc:
#     print(el)
#     print(el.ent_type_)

for i in range(0, 3):
  for tweet in api.user_timeline('stoolpresidente', page = i):
    for node in preprocess(tweet.text):
      if type(node) == nltk.tree.Tree:
        for tup in node:
          ne = (tup[0])
          if ne.lower() == 'first' or ne.lower() == 's' or ne.lower == 'yup' or ne.lower == 'yeah':
            continue
          nes.append(ne.lower())

print(nes)

symbols = []

con = sqlite3.connect('./data/symbols.db')
cursor = con.cursor()
query = 'SELECT * FROM symbols'

for ne in nes:
  for row in cursor.execute(query):
    name = row[1]
    if ne.lower() in name:
      print(ne.lower())
      print(name)
      symbols.append(row[0])


print(symbols)

cursor.close()










# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(track=['lebron'])
