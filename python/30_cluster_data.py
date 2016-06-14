# -*- coding: utf-8 -*-
"""
Cluster Yelp tip and review data

@author: MariaAthena
"""


import pandas as pd
import numpy as np
import pickle

import matplotlib.cm as cm
import seaborn as sns

import sklearn
from sklearn import cluster
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.decomposition import PCA

from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import dendrogram, linkage


df_montr = pickle.read('../parsed_data/cosim_montreal.feather', 'rb')
df_pitts = pickle.read('../parsed_data/cosim_pittsburgh.feather', 'rb')
df_edinb = pickle.read('../parsed_data/cosim_edinburgh.feather', 'rb')


# Convert the cosim columns into numpy arrays
montr_data = np.array(df_montr.ix[:,:])
pitts_data = np.array(df_pitts.ix[:,:])
edinb_data = np.array(df_edinb.ix[:,:])


# Compute the K Nearest Neighbours for each city





