import string
import sqlite3

# TODO - STRIP WHITESPACE

def strip_punc(s):
  return s.translate(str.maketrans('', '', string.punctuation))

def stock_words(s):
  words_to_strip = ['tech', 'technology', 'technologies', 'common', 'company', 'bioscience', 'biosciences', 'class', 'corp', 'inc', 'corporation', 'bancorporation', 'NA', 'acquisition', 'technologies', 'pharmaceuticals', 'test', 'stock']
  for word in words_to_strip:
    s = s.replace(word, '')
  return s.lstrip()

con = sqlite3.connect('../data/symbols.db')
cursor = con.cursor()

with open('../data/nasdaqlisted.txt', 'r') as symbols:
  for line in symbols:
    line = line.split('|')
    symbol = line[0].lower()
    name = line[1].split('-')[0].lower()
    # symbol = strip_punc(symbol).lstrip()
    # name = strip_punc(name)
    # name = stock_words(name).lstrip()
    insert_columns = "INSERT INTO symbols ('symbol', 'name')"
    insert_values = "VALUES (\"" + symbol + "\", \"" + name + "\");"
    insert_query = insert_columns + insert_values
    cursor.execute(insert_query)

con.commit()
cursor.close()