# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:17:44 2016

@author: Mia
"""
# Prepare environment and load data ------------------------------------------
import pandas as pd
import numpy as np
import nltk
import re
import random


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

types=[]
for i in range(0,len(business_df.categories)):
    for item in business_df.categories[i]:
        types.append(item)

unique_types = set(sorted(types))


        


