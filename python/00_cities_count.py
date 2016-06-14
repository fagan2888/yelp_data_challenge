# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:50:38 2016

@author: Mia
"""

import pandas as pd    




# Read data file into a python array
with open('/Users/Mia/Downloads/data/yelp_academic_dataset_business.json', 'rb') as business_f:
	business_data = business_f.readlines()

# remove the trailing "\n" from each line
business_data = map(lambda x: x.rstrip(), business_data)
# put individual business JSON objects into list
business_data_json = "[" + ','.join(business_data) + "]"

# Create pandas df
business_df = pd.read_json(business_data_json)
business_df = business_df[['city','business_id','state','type','latitude','longitude','stars','categories']]






# Read data file into a python array
with open('/Users/Mia/Downloads/data/yelp_academic_dataset_review.json', 'rb') as review_f:
	review_data = review_f.readlines()

# remove the trailing "\n" from each line
review_data = map(lambda x: x.rstrip(), review_data)
# put individual business JSON objects into list
review_data_json = "[" + ','.join(review_data) + "]"

# Create pandas df
review_df = pd.read_json(review_data_json)
review_df = review_df[['business_id', 'user_id', 'date', 'text']]

"""
review_df.text = tip_df.text.apply(lambda x: norm_corpus(x))
review_df.text = tip_df.text.apply(lambda x: review_vector(x))
"""


dataframe = pd.merge(review_df, business_df, on ='business_id')
grouped = dataframe.groupby(['city'], sort = True).count()
grouped.sort_values('text',ascending=False)