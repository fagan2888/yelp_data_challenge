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



# GLENDALE
glendale = cosine_df[cosine_df['city']== 'Glendale']
glendale = glendale.reset_index(drop=True)


cosine_matrix_glendale = np.zeros((len(glendale['text']),len(glendale['text'])))
for i in range(0,len(glendale['text'])):
    print i,'/',len(glendale)
    for j in range(0,len(glendale['text'])):
        cosine_matrix_glendale[i][j] = similarity(glendale['text'].values[i], glendale['text'].values[j])

glendale_matrix = pd.DataFrame(cosine_matrix_glendale)
glendale_matrix = glendale_matrix.reset_index(drop=True)
print 'matrix done'

cosim_glendale = pd.concat([glendale,glendale_matrix], axis=1)

try:
    cosim_glendale.to_pickle('../parsed_data/cosim_glendale.pkl')
    print 'pkl written'
except (SystemError):
    cosim_glendale_sample = cosim_glendale.sample(frac = 0.6, replace = True)
    cosim_glendale_sample.to_pickle('../parsed_data/cosim_glendale.pkl')
    print 'pkl written'



# EDINBURGH
edinburgh = cosine_df[cosine_df['city']== 'Edinburgh']
edinburgh = edinburgh.reset_index(drop=True)


cosine_matrix_edinburgh = np.zeros((len(edinburgh['text']),len(edinburgh['text'])))
for i in range(0,len(edinburgh['text'])):
    print i,'/',len(edinburgh)
    for j in range(0,len(edinburgh['text'])):
        cosine_matrix_edinburgh[i][j] = similarity(edinburgh['text'].values[i], edinburgh['text'].values[j])

edinburgh_matrix = pd.DataFrame(cosine_matrix_edinburgh)
edinburgh_matrix = edinburgh_matrix.reset_index(drop=True)
print 'matrix done'

cosim_edinburgh = pd.concat([edinburgh,edinburgh_matrix], axis=1)

cosim_edinburgh.to_pickle('../parsed_data/cosim_edinburgh.pkl')
print 'pkl written'



# KARLSRUHE
karlsruhe = cosine_df[cosine_df['city']== 'Karlsruhe']
karlsruhe = karlsruhe.reset_index(drop=True)


cosine_matrix_karlsruhe = np.zeros((len(karlsruhe['text']),len(karlsruhe['text'])))
for i in range(0,len(karlsruhe['text'])):
    print i,'/',len(karlsruhe)
    for j in range(0,len(karlsruhe['text'])):
        cosine_matrix_karlsruhe[i][j] = similarity(karlsruhe['text'].values[i], karlsruhe['text'].values[j])

karlsruhe_matrix = pd.DataFrame(cosine_matrix_karlsruhe)
karlsruhe_matrix = karlsruhe_matrix.reset_index(drop=True)
print 'matrix done'

cosim_karlsruhe = pd.concat([karlsruhe,karlsruhe_matrix], axis=1)
cosim_karlsruhe.to_pickle('../parsed_data/cosim_karlsruhe.pkl')
print 'pkl written'
