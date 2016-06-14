# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:07:19 2016

@author: Mia
"""

# Prepare environment and load data ------------------------------------------
import pandas as pd
import numpy as np

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
montreal = montreal.reset_index(drop=True)


cosine_matrix_montreal = np.zeros((len(montreal['text']),len(montreal['text'])))
for i in range(0,len(montreal['text'])):
    for j in range(0,len(montreal['text'])):
        cosine_matrix_montreal[i][j] = similarity(montreal['text'].values[i], montreal['text'].values[j])

montreal_matrix = pd.DataFrame(cosine_matrix_montreal)
montreal_matrix = montreal_matrix.reset_index(drop=True)

cosim_montreal = pd.concat([montreal,montreal_matrix], axis=1)

cosim_montreal.to_pickle('../parsed_data/cosim_montreal.pkl')
print 'pkl written'


# EDINBURGH
edinburgh = cosine_df[cosine_df['city']== 'Edinburgh']
edinburgh = edinburgh.reset_index(drop=True)


cosine_matrix_edinburgh = np.zeros((len(edinburgh['text']),len(edinburgh['text'])))
for i in range(0,len(edinburgh['text'])):
    for j in range(0,len(edinburgh['text'])):
        cosine_matrix_edinburgh[i][j] = similarity(edinburgh['text'].values[i], edinburgh['text'].values[j])

edinburgh_matrix = pd.DataFrame(cosine_matrix_edinburgh)
edinburgh_matrix = edinburgh_matrix.reset_index(drop=True)

cosim_edinburgh = pd.concat([edinburgh,edinburgh_matrix], axis=1)

cosim_edinburgh.to_pickle('../parsed_data/cosim_edinburgh.pkl')
print 'pkl written'


# PITTSBURGH
pittsburgh = cosine_df[cosine_df['city']== 'Pittsburgh']
pittsburgh = pittsburgh.reset_index(drop=True)


cosine_matrix_pittsburgh = np.zeros((len(pittsburgh['text']),len(pittsburgh['text'])))
for i in range(0,len(pittsburgh['text'])):
    for j in range(0,len(pittsburgh['text'])):
        cosine_matrix_pittsburgh[i][j] = similarity(pittsburgh['text'].values[i], pittsburgh['text'].values[j])

pittsburgh_matrix = pd.DataFrame(cosine_matrix_pittsburgh)
pittsburgh_matrix = pittsburgh_matrix.reset_index(drop=True)

cosim_pittsburgh = pd.concat([pittsburgh,pittsburgh_matrix], axis=1)
cosim_pittsburgh.to_pickle('../parsed_data/cosim_pittsburgh.pkl')
print 'pkl written'
