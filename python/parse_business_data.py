# -*- coding: utf-8 -*-
"""
Read in Yelp data in pandas df

@author: MariaAthena
"""

import pandas as pd
import json


# read the entire file into a python array
with open('../data/yelp_academic_dataset_business.json', 'rb') as f:
	bus_data = f.readlines()


# remove the trailing "\n" from each line
bus_data = map(lambda x: x.rstrip(), bus_data)

# put individual business JSON objects into list
data_json = "[" + ','.join(bus_data) + "]"

bus_df = pd.read_json(data_json)

