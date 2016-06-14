# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:22:39 2016

@author: Mia
"""


import pandas as pd
import matplotlib.pyplot as plt

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



x = monthly_montreal_df['indices_sum'].values.tolist()
y = range(1,len(monthly_montreal_df))


plt.plot(x, y, 'ro')

plt.ylabel('some numbers')
plt.show()
              
                

"""
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
"""                   
                                   
                                   