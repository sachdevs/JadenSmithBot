from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize

with open ("morejaden.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

tokens = word_tokenize(data.encode('utf-8'))
print tokens