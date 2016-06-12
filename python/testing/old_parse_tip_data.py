# -*- coding: utf-8 -*-
"""
Parse Yelp tip data

@author: MariaAthena
"""

import pandas as pd
import numpy as np
import json
import re
import nltk

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# Read data file into a python array
with open('../data/yelp_academic_dataset_tip.json', 'rb') as f:
	bus_data = f.readlines()

# remove the trailing "\n" from each line
bus_data = map(lambda x: x.rstrip(), bus_data)
# put individual business JSON objects into list
data_json = "[" + ','.join(bus_data) + "]"

# Create pandas df
bus_df = pd.read_json(data_json)


## Helper functions to normalise and vectorise text

# x = nltk.collocations(text)

# Convert all words to lowercase, remove punctuation, tokenise and stem
# and remove stopwords, threshold = 10%
def norm_corpus(document_list):
    norm_doc_list = []
    
    # lowercase
    document_list = [word.lower() for word in document_list]

    
    # remove symbols in text
    symbols = ",.?!"
    for sym in symbols:
        document_list = [word.replace(sym,'') for word in document_list]
    
    
    # loop through each string i.e. review in the column
    for doc in document_list:
        doc = nltk.word_tokenize(doc)
        
        # remove stopwords
        doc = [word for word in doc if word not in stopwords.words('english')]
        
        # stem words
        stemmer = SnowballStemmer("english")
        doc = [stemmer.stem(word) for word in doc]
        
        # make tokenised text one string
        norm_doc = " ".join(doc)
        norm_doc_list.append(norm_doc)
    
    return norm_doc_list



# Vectorise normalised text to vector including only nouns and adjectives
def review_vector(norm_doc_list):
    review_list = []

    # select all words categorised as nouns or adjectives
    # loop through each string i.e. review in the df column
    for doc in norm_doc_list:
        review_keyword_list = []
        doc = nltk.word_tokenize(doc)
        # create tuple for each word in list: (word, tag)
        token_category = nltk.pos_tag(doc)
        
        
        for word, tag in token_category:    
            
            # nouns
            if (tag == 'NN' or tag == 'NNS' or tag == 'NNP' or tag == 'NNPS'):
                review_keyword_list.append(word)
                
            # adjectives
            elif (tag == 'JJ' or tag == 'JJS' or tag == 'JJP' or tag == 'JJPS'):
                review_keyword_list.append(word)
            else:
                pass     
        
        review_keywords = " ".join(review_keyword_list)
        review_list.append(review_keywords)
        
        # vectorise string
        WORD = re.compile(r'\w+')
        review_vector = [Counter(WORD.findall(word)) for word in review_list]
    
    
    return review_vector




# Normalise and vectorise tip column in datafram
output_df = bus_df[['business_id', 'user_id', 'date']]  
output_df['tip'] = norm_corpus(bus_df.text)
print "tip text normalised, next: vectorise"
output_df.tip = review_vector(output_df.tip)

output_df.to_csv(open('parsed_tip_data.csv', 'wb'), index=False)
