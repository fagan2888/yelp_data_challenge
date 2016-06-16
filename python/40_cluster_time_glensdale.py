# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:22:39 2016

@author: Mia
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime

cluster_glendale =  pd.read_pickle('../parsed_data/indexed_glendale.pkl')

cluster_glendale = cluster_glendale.set_index(['date'])
months = len(pd.DataFrame.groupby(cluster_glendale,
                                   by=[cluster_glendale.index.year, 
                                       cluster_glendale.index.month]))
                                     
# glendale
                                     
plot_x=[];
plot_y =[];
colors = ['r', 'g', 'y', '#d11141', '#00b159', '#00aedb','#f37735', '#ffc425']
for i in range(0,len(cluster_glendale['kmean_index'].unique())):
    print i


    # To read in file
    cluster_glendale =  pd.read_pickle('../parsed_data/indexed_glendale.pkl')
    
    # To group by same month in year make date column index
    cluster_glendale = cluster_glendale.set_index(['date'])
    cluster_glendale = cluster_glendale[cluster_glendale.kmean_index == i]
     
    # To perform groupby, summinng up cluster indices per month
    monthly_glendale = pd.DataFrame.groupby(cluster_glendale,
                                   by=[cluster_glendale.index.year, 
                                       cluster_glendale.index.month], sort = True)['kmean_index'].count()
    #print monthly_glendale
                                                      
    monthly_glendale_df = pd.DataFrame(monthly_glendale)               
    monthly_glendale_df.columns = ['indices_sum']
    #print monthly_glendale_df.head()

    y = monthly_glendale_df['indices_sum'].values.tolist()
    #print y
    
    # To plot all clusters later    
    plot_y.append(y)    
    
    
    x = []
    for j in range(0,len(monthly_glendale)):
        x.append(datetime.datetime(monthly_glendale.index[j][0],monthly_glendale.index[j][1],1))
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
             

                              
                                   