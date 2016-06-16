# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:54:43 2016

@author: Mia
"""

import pandas as pd
from collections import Counter

cluster_edinburgh =  pd.read_pickle('../parsed_data/indexed_glendale.pkl')

wordcloud_index1 = cluster_edinburgh[cluster_edinburgh.kmean_index == 2]

cloud1 = sum(wordcloud_index1.text, Counter())
cloud1.most_common(150)