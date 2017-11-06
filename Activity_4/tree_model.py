#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 2 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero 
López-Sepúlveda
"""


import sys
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


### 1. Load the data asigned
try:
    data_features = pd.read_csv('../Data/dengue_features_train.csv')
    data_labels = pd.read_csv('../Data/dengue_labels_train.csv')
    data = pd.merge(data_features, data_labels, on=['city','year','weekofyear'])
    
    data = data.head(347)
    
    data = data.fillna(0)
    
except:
    print("Error while loading the data")
    sys.exit()
    
# Remove outliers 87, 139
data = data.drop([87,139])


### 2. Feature selection
features_names = ['year', 'weekofyear',
                  'ndvi_se', 'ndvi_sw',
                  'reanalysis_max_air_temp_k', 'reanalysis_air_temp_k',
                  'reanalysis_specific_humidity_g_per_kg', 'station_max_temp_c',
                  'station_precip_mm', 'reanalysis_sat_precip_amt_mm']

features = data[features_names]
labels = data['total_cases']


### 3. Build the deccision tree
# Parametrization
regressor = DecisionTreeRegressor(criterion='mse', max_depth=2, random_state=0)

# Fit
regressor.fit(features, labels)

# Feature Relevances
print 'Feature Relevancies'
list1 = zip(features, regressor.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

# Cross validation analysis
total_scores = []
for i in range(2, 30):
    regressor = DecisionTreeRegressor(criterion='mse', max_depth=i)
    regressor.fit(features, labels)
    scores = -cross_val_score(regressor, features,
            labels, scoring='neg_mean_absolute_error', cv=10)
    total_scores.append(scores.mean())

plt.plot(range(2,30), total_scores, marker='o')
plt.xlabel('max_depth')
plt.ylabel('cv score')
plt.show()    