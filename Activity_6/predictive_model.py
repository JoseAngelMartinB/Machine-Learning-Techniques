#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu 17 Nov 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero
López-Sepúlveda
"""

import sys
import pandas as pd



### 1. Load the data

try:
    data_features = pd.read_csv('../Data/dengue_features_train.csv')
    data_labels = pd.read_csv('../Data/dengue_labels_train.csv')
    data = pd.merge(data_features, data_labels, on=['city', 'year', 'weekofyear'])

    data_features_test = pd.read_csv('../Data/dengue_features_test.csv')

except:
    print("Error while loading the data.")
    sys.exit()



### 2. Missing Values

# Perform linear interpolation where there is missing data
data = data.interpolate()

# Remove outliers (they have lot of missing data)
outliers_sj = [89, 141, 401, 453, 713, 765]
outliers_iq = [184, 236, 444, 496]
outliers = outliers_sj + [x + 936 for x in outliers_iq]
data = data.drop([x - 2 for x in outliers]) # Because element index is element - 2



### 3. Feature Selection

features_selected_sj = ['year', 'weekofyear',
                      'reanalysis_dew_point_temp_k',
                      'reanalysis_relative_humidity_percent',
                      'reanalysis_precip_amt_kg_per_m2',
                      'ndvi_se',
                      'reanalysis_specific_humidity_g_per_kg']

features_selected_iq = ['year', 'weekofyear',
                      'reanalysis_min_air_temp_k',
                      'reanalysis_tdtr_k',
                      'station_avg_temp_c',
                      'reanalysis_relative_humidity_percent',
                      'reanalysis_precip_amt_kg_per_m2']

features_sj = data.loc[data['city'] == 'sj'][features_selected_sj]
features_iq = data.loc[data['city'] == 'iq'][features_selected_iq]
labels = data['total_cases']



### 4. Parametrization

# Cross validation analysis


'''
- Normalization/Scalation or Nothing. 
- Distance function: euclidean ....
- K value
- uniform / distance weighting scheme (using the knowledge extracted in cross-validation)
'''









### 5. Execute kNN and make predictions


