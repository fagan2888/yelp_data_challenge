# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:50:38 2016

@author: Mia
"""

import pandas as pd    
import feather



# Read data file into a python array
review_df = feather.read_dataframe('../parsed_data/filtered_review_data.feather', 'rb')

review_grouped = review_df.groupby(['city'], sort = True).count()
review_cities = review_grouped.sort_values('text',ascending=False)

# Read data file into a python array
tip_df = feather.read_dataframe('../parsed_data/filtered_tip_data.feather', 'rb')

tip_grouped = tip_df.groupby(['city'], sort = True).count()
tip_cities = tip_grouped.sort_values('text',ascending=False)