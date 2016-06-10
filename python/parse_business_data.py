# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:46:24 2016

Read in Yelp data in pandas df

@author: MariaAthena
"""

import pandas as pd
import json


with open('yelp_academic_dataset_business.json', 'rb') as f:
	bus_data = f.readlines()


bus_data = f.readlines()
bus_data = map(lambda x: x.rstrip(), data)
data_json = "[" + ','.join(bus_data) + "]"

bus_df = pd.read_json(data_json)

