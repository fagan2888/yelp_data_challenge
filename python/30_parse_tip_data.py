# -*- coding: utf-8 -*-
"""
Cluster Yelp tip and review data

@author: MariaAthena
"""


import pandas as pd
import numpy as np
import feather
import re
import nltk


df_montr = feather.read_dataframe('../parsed_data/cosim_montreal.feather', 'rb')
df_pitts = feather.read_dataframe('../parsed_data/cosim_pittsburgh.feather', 'rb')
df_edinb = feather.read_dataframe('../parsed_data/cosim_edinburgh.feather', 'rb')

