# -*- coding: utf-8 -*-
"""
Cluster Yelp tip and review data

@author: MariaAthena
"""


import pandas as pd
import numpy as np

import sklearn
from sklearn import cluster
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.decomposition import PCA

from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import dendrogram, linkage


df = pd.read_pickle('../parsed_data/cosim_montreal.pkl')
# df = pd.read_pickle('../parsed_data/cosim_pittsburgh.pkl')
# df = pd.read_pickle('../parsed_data/cosim_edinburgh.pkl')


# Convert the cosim columns into numpy arrays
data = np.array(df.ix[:,6:])

# Compute the K Nearest Neighbours
# K-Means for k=8
n_clusters2=8
k_means = cluster.KMeans(n_clusters=n_clusters2, init='k-means++')
k_means.fit(data) # Computes k-means

df['kmean_index'] = k_means.labels_
# output_df = df.drop(df.ix[:,6:-1])
output_df = df[['business_id', 'text', 'date', 'city', 'latitude', 'longitude', 'kmean_index']]

# Output parsed data to feather format file
output_df.to_pickle('../parsed_data/indexed_montreal.pkl')
