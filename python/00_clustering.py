# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:36:03 2016

@author: Mia
"""

# Prepare environment and load data ------------------------------------------
import pandas as pd
import numpy as np
import nltk
import re
import random
import csv


from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.cluster import KMeans



# Calculate the cosine similarity of two vectors 
def similarity(vect1, vect2):
    numerator =  len(list(set(vect1) & set(vect2)))
    denom = len(list(set(vect1) | set(vect2)))
    if not denom:
        sim = 0
    else:
        sim = round(float(numerator)/denom,10)
    return sim   
    
# Convert all words to lowercase, remove punctuation, tokenise and stem
# and remove stopwords, threshold = 10%
def norm_corpus(document):

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
    
        
        

# Read data file into a python array
with open('../data/yelp_academic_dataset_business.json', 'rb') as business_f:
	business_data = business_f.readlines()

# remove the trailing "\n" from each line
business_data = map(lambda x: x.rstrip(), business_data)
# put individual business JSON objects into list
business_data_json = "[" + ','.join(business_data) + "]"

# Create pandas df
business_df = pd.read_json(business_data_json)
business_df = business_df[['city','business_id','state','type','latitude','longitude','stars','categories']]




# Read data file into a python array
with open('../data/yelp_academic_dataset_tip.json', 'rb') as tip_f:
	tip_data = tip_f.readlines()

# remove the trailing "\n" from each line
tip_data = map(lambda x: x.rstrip(), tip_data)
# put individual business JSON objects into list
tip_data_json = "[" + ','.join(tip_data) + "]"



# Create pandas df
tip_df = pd.read_json(tip_data_json)
tip_df = tip_df[['business_id', 'user_id', 'date', 'text']]
"""
tip_df.text = tip_df.text.apply(lambda x: norm_corpus(x))
tip_df.text = tip_df.text.apply(lambda x: review_vector(x))
"""


dataframe = pd.merge(tip_df, business_df, on ='business_id')


grouped = dataframe.groupby(['city'], sort = True).count()



for k in range(0,len(dataframe['state'].unique())-1):

    state = dataframe['state'].unique()[k]
    state = state.encode('ascii','ignore')


    year2009 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2009-04-15')) & (grouped.get_group('PA')['date'] <= np.datetime64('2009-12-31'))].copy()
    year2010 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2010-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2010-12-31'))].copy()
    year2011 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2011-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2011-12-31'))].copy()
    year2012 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2012-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2012-12-31'))].copy()
    year2013 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2013-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2013-12-31'))].copy()
    year2014 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2014-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2014-12-31'))].copy()
    year2015 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2015-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2015-12-31'))].copy()
    year2016 = grouped.get_group('PA').loc[(grouped.get_group('PA')['date'] > np.datetime64('2016-01-01')) & (grouped.get_group('PA')['date'] <= np.datetime64('2016-12-31'))].copy()






    num_clusters = 5
    
    

    cosine_matrix2009 = np.zeros((len(year2009['text']),len(year2009['text'])))
    for i in range(0,len(year2009['text'])):
        for j in range(0,len(year2009['text'])):
            cosine_matrix2009[i][j] = similarity(year2009['text'].values[i], year2009['text'].values[j])
    
    kmeans2009 = KMeans(n_clusters=num_clusters, init='k-means++')
    kmeans2009.fit(cosine_matrix2009)
    
    labels2009 = kmeans2009.labels_
    labels2009 = pd.DataFrame(labels2009)
    labels2009.columns = ['cluster_idx']
    
    centroids2009 = kmeans2009.cluster_centers_
    year2009 = year2009.reset_index(drop=True)

    frame2009 = pd.concat([year2009, labels2009], ignore_index=False, axis=1)





    
    




#min(dataframe.date)
#Timestamp('2009-04-15 00:00:00')
#
#max(dataframe.date)
#Timestamp('2016-01-07 00:00:00')
