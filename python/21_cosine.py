# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:07:19 2016

@author: Mia
"""

# Prepare environment and load data ------------------------------------------
import pandas as pd
import numpy as np
import nltk
import re
import feather


from collections import Counter




# Calculate the cosine similarity of two vectors 
def similarity(vect1, vect2):
    numerator =  len(list(set(vect1) & set(vect2)))
    denom = len(list(set(vect1) | set(vect2)))
    if not denom:
        sim = 0
    else:
        sim = round(float(numerator)/denom,10)
    return sim   
    
    
# Read data file into a pandas dataframe
#read_df = feather.read_dataframe('../parsed_data/parsed_tip_data.feather', 'rb')
cosine_df =  pd.read_pickle('../parsed_data/all_parsed_data.pkl')



# MONTREAL
montreal = cosine_df[cosine_df['city']== 'Montreal']

cosine_matrix_montreal = np.zeros((len(montreal['text']),len(montreal['text'])))
for i in range(0,len(montreal['text'])):
    for j in range(0,len(montreal['text'])):
        cosine_matrix_montreal[i][j] = similarity(montreal['text'].values[i], montreal['text'].values[j])



# EDINBURGH
edinburgh = cosine_df[cosine_df['city']== 'Edinburgh']

cosine_matrix_edinburgh = np.zeros((len(edinburgh['text']),len(edinburgh['text'])))
for i in range(0,len(edinburgh['text'])):
    for j in range(0,len(edinburgh['text'])):
        cosine_matrix_edinburgh[i][j] = similarity(edinburgh['text'].values[i], edinburgh['text'].values[j])



# PITTSBURGH
pittsburgh = cosine_df[cosine_df['city']== 'Pittsburgh']

cosine_matrix_pittsburgh = np.zeros((len(pittsburgh['text']),len(pittsburgh['text'])))
for i in range(0,len(pittsburgh['text'])):
    for j in range(0,len(pittsburgh['text'])):
        cosine_matrix_pittsburgh[i][j] = similarity(pittsburgh['text'].values[i], pittsburgh['text'].values[j])

