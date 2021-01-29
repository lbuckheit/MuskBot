# TODO - Fine tune the NER

import nltk

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag, StanfordNERTagger
from nltk.chunk import ne_chunk


def preprocess(tweet):
  # words = [word_tokenize(word) for word in tweet]
  # words = list(chain(*words))
  # words = ne_chunk(words)

  st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
  tokenized_text = word_tokenize(tweet)
  classified_text = st.tag(tokenized_text)

  return classified_text

tweets = []
with open ('test_tweets.txt', 'r', encoding="utf-8") as f:
  for line in f:
    tweets.append(line)

spacy_pn = []
spacy_ne = []
nltk_ne = []
nlp = spacy.load("en_core_web_sm")

for tweet in tweets:
  '''
  doc = nlp(tweet)

  # spaCy proper nouns
  for token in doc:
    if token.pos_ == "PROPN":
      entity = token.text
      if entity[0] == '@':
        entity = entity[1:]
        spacy_pn.append(entity)

  # spacy ORG type entities
  for ent in doc.ents:
      if ent.label_ != 'ORG':
        continue

      spacy_ne.append(ent.text)

  # NLTK NER
  for node in preprocess(tweet):
    if type(node) == nltk.tree.Tree:
      print(node)
      # for tup in node:
      #   ne = (tup[0])
      #   nltk_ne.append(ne)
  '''

  print(preprocess(tweet))

# spacy_pn = set(spacy_pn)
# spacy_ne = set(spacy_ne)
# nltk_ne = set(nltk_ne)
# print(spacy_pn)
# print(spacy_ne)
# print(nltk_ne)
