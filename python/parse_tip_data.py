# -*- coding: utf-8 -*-
"""
Read in Yelp data in pandas df

@author: MariaAthena
"""

import pandas as pd
import json
import collections

from nltk.stem.porter import PorterStemmer # http://tartarus.org/martin/PorterStemmer/
from nltk.stem import WordNetLemmatizer # http://textanalysisonline.com/nltk-wordnet-lemmatizer


# Read data file into a python array
with open('../data/yelp_academic_dataset_tip.json', 'rb') as f:
	bus_data = f.readlines()

# remove the trailing "\n" from each line
bus_data = map(lambda x: x.rstrip(), bus_data)
# put individual business JSON objects into list
data_json = "[" + ','.join(bus_data) + "]"

# Create pandas df
bus_df = pd.read_json(data_json)


# Helper functions for preparing the text data

# Convert all to lowercase and remove punctuation
def clean_corpus(word_list):
    
    clean_words = []
    word_list = [token.lower() for token in tokens]



# Create list of words occurring too frequently, threshold: 10%
def stop_words(word_list):

    stop_list = []
    counts = collections.Counter(word_list)
    frequency = counts[word] / float(len(word_list))

    for word in word_list:
        single_word_list = word_list.unique()

        if frequency > 0.1:
            stop_list.append(word)

    return (single_word_list, stop_list)


# Lemmatise 



# Helper function to extract nouns from a Python string object
def extract_nouns(txt):
    nouns = []

    # create list of words in a text, taking out punctuations, symbols etc.
    words = nltk.word_tokenize(txt)
    # categorise all words in text with tags
    tags = nltk.pos_tag(words)

    # select all words categorised as nouns
    for word, pos in tags:
        if (pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS'):
            nouns.append(word.lower())

    return nouns


# Helper function to convert text to vector
WORD = re.compile(r'\w+')

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)




