# -*- coding: utf-8 -*-
"""
Parse Yelp review data
@author: MariaAthena
"""
# Output of this file has to be pickle otherwise dictionary/vector information lost

import re
import nltk
import pandas as pd
import feather

from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# Read review data file into a pandas dataframe
read_df = feather.read_dataframe('../parsed_data/filtered_review_data.feather', 'rb')
#read_df = pd.read_pickle('../parsed_data/filtered_review_data.pkl')

## Helper functions to normalise and vectorise text

# Convert all words to lowercase, remove punctuation, tokenise and stem
# and remove stopwords, threshold = 10%
def norm_corpus(document):

    # unicode decode
    document = document.decode('utf-8')

    # lowercase and remove symbols
    tokenizer = RegexpTokenizer(r'\w+')
    doc_tokens = tokenizer.tokenize(document.lower())
        
    # remove stopwords
    doc_tokens = [word for word in doc_tokens if word not in stopwords.words('english')]
        
    # stem words
    stemmer = SnowballStemmer("english")
    doc_stem = [stemmer.stem(word) for word in doc_tokens]
        
    # make tokenised text one string
    norm_doc = " ".join(doc_stem)
    
    
    return norm_doc



# Vectorise normalised text to vector including only nouns and adjectives
# Vectorise keywords from normalised text to vector including only nouns and adjectives
def review_vector(norm_doc):

    # select all words categorised as nouns or adjectives
    # loop through each string i.e. review in the df column
    review_keyword_list = []
    doc = nltk.word_tokenize(norm_doc)

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
        
    # vectorise string
    WORD = re.compile(r'\w+')
    review_vector = Counter(WORD.findall(review_keywords))
    
    
    return review_vector


# Only keep businesses with more than 3 stars
read_df = read_df[read_df.stars > 3]

# Normalise and vectorise tip column in datafram
output_df = read_df.ix[:,['business_id', 
                          'user_id', 
                          'date', 
                          'stars',
                          'text',
                          'city',
                          'latitude',
                          'longitude']]
                          
output_df.text = output_df.text.apply(lambda x: norm_corpus(x))
print "review text normalised, next: vectorise"
output_df.text = output_df.text.apply(lambda x: review_vector(x))
print "review text vectorised"

output_df.to_pickle('../parsed_data/parsed_review_data.pkl')
print 'pkl written'

#feather.write_dataframe(output_df, '../parsed_data/parsed_review_data.feather')
#print 'feather writte'