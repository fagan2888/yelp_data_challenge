# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:06:22 2016

@author: Mia
"""

import pandas as pd

parsed_tip = pd.read_pickle('../parsed_data/parsed_tip_data.pkl')
parsed_review = pd.read_pickle('../parsed_data/parsed_tip_data.pkl')

parsed_tip = parsed_tip.ix[:,['business_id','text','date','latitude','longitude','city']]
parsed_review = parsed_review.ix[:,['business_id','text','date','latitude','longitude','city']]

frames = [parsed_tip, parsed_review]

tip_review = pd.concat(frames)

tip_review.to_pickle('../parsed_data/all_parsed_data.pkl')
print 'pkl written'
