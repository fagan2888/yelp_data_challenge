# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:42:30 2016

@author: Mia
"""


import pandas as pd
import matplotlib.pyplot as plt
import datetime

cluster_edinburgh =  pd.read_pickle('../parsed_data/indexed_edinburgh.pkl')

cluster_edinburgh = cluster_edinburgh.set_index(['date'])
months = len(pd.DataFrame.groupby(cluster_edinburgh,
                                   by=[cluster_edinburgh.index.year, 
                                       cluster_edinburgh.index.month]))
                                     
# EDINBURGH
                                     
plot_x=[];
plot_y =[];
colors = ['r', 'g', 'y', '#d11141', '#00b159', '#00aedb','#f37735', '#ffc425']
for i in range(0,len(cluster_edinburgh['kmean_index'].unique())):
    print i


    # To read in file
    cluster_edinburgh =  pd.read_pickle('../parsed_data/indexed_edinburgh.pkl')
    
    # To group by same month in year make date column index
    cluster_edinburgh = cluster_edinburgh.set_index(['date'])
    cluster_edinburgh = cluster_edinburgh[cluster_edinburgh.kmean_index == i]
     
    # To perform groupby, summinng up cluster indices per month
    monthly_edinburgh = pd.DataFrame.groupby(cluster_edinburgh,
                                   by=[cluster_edinburgh.index.year, 
                                       cluster_edinburgh.index.month], sort = True)['kmean_index'].count()
    #print monthly_montreal
                                                      
    monthly_edinburgh_df = pd.DataFrame(monthly_edinburgh)               
    monthly_edinburgh_df.columns = ['indices_sum']
    #print monthly_edinburgh_df.head()

    y = monthly_edinburgh_df['indices_sum'].values.tolist()
    #print y
    
    # To plot all clusters later    
    plot_y.append(y)    
    
    
    x = []
    for j in range(0,len(monthly_edinburgh)):
        x.append(datetime.datetime(monthly_edinburgh.index[j][0],monthly_edinburgh.index[j][1],1))
    #print x

    # To plot all clusters later
    plot_x.append(x)
    
    # To plot single clusters
    fig, ax = plt.subplots()
    # To lift plot
    ax.margins(0.01)
    # To iterate over colors
    ax.plot_date(x, y, '-',color = colors[i])
    # To set same time frame
    ax.set_xlim([datetime.datetime(2009,1,1),datetime.datetime(2015,11,1)])


# To plot all clusters at once
fig, ax = plt.subplots()
ax.margins(0.01)
for k in range(len(plot_x)):
    ax.plot_date(plot_x[k], plot_y[k], '-',color = colors[k])
plt.ylabel('Cluster Size')
plt.show()
    
# Should we divide cluster size by average reviews to cancel for the effect of more internet users?
             

                              
                                   