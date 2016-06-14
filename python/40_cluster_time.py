# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:22:39 2016

@author: Mia
"""


import pandas as pd

# change filename to file from maria
cluster_montreal =  pd.read_pickle('../parsed_data/index_montreal.pkl')


# MONTREAL
# Group by same month in year 
# make date column index
cluster_montreal = cluster_montreal.set_index(['date'])


# perform groupby, summinng up dummies for count
monthly_montreal = pd.DataFrame.groupby(cluster_montreal,
                               by=[cluster_montreal.index.year, 
                                   cluster_montreal.index.month,
                                   cluster_montreal.longitude], sort = True)['kmean_index'].count()
                                                    
monthly_montreal_df = pd.DataFrame(monthly_montreal)               
monthly_montreal_df.columns = ['indices_sum']                    
                                   
                                   
                                   