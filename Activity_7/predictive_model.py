#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri 24 Nov 2017

@author: José Ángel Martín Baos, Óscar Pérez Galán, Miguel Ampuero
López-Sepúlveda
"""

import sys
import pandas as pd

from sklearn import neighbors
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing



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
data_features_test = data_features_test.interpolate()

# Remove outliers (they have lot of missing data)
outliers_sj = [89, 141, 401, 453, 713, 765]
outliers_iq = [184, 236, 444, 496]
outliers = outliers_sj + [x + 936 for x in outliers_iq]
data = data.drop([x - 2 for x in outliers]) # Because element index is element - 2



### 3. Feature Selection

features_selected_sj = ['weekofyear',
                      'reanalysis_dew_point_temp_k',
                      'reanalysis_relative_humidity_percent',
                      'reanalysis_precip_amt_kg_per_m2',
                      'ndvi_se',
                      'reanalysis_specific_humidity_g_per_kg']

features_selected_iq = ['weekofyear',
                      'reanalysis_min_air_temp_k',
                      'reanalysis_specific_humidity_g_per_kg',
                      'reanalysis_precip_amt_kg_per_m2']

features_sj = data.loc[data['city'] == 'sj'][features_selected_sj]
features_iq = data.loc[data['city'] == 'iq'][features_selected_iq]
labels_sj = data.loc[data['city'] == 'sj']['total_cases']
labels_iq = data.loc[data['city'] == 'iq']['total_cases']

# Not use first years
features_sj = features_sj.tail(650)
features_iq = features_iq.tail(300)
labels_sj = labels_sj.tail(650)
labels_iq = labels_iq.tail(300)



### 4. Execute the regresor and make predictions

## San Juan
data_features_test_sj = data_features_test.loc[data_features_test['city'] == 'sj']

# Parametrization
n_estimators = 50
max_depth = None
max_features = len(features_selected_sj)

# Random Forest regressor
regressor_sj = RandomForestRegressor(n_estimators= n_estimators, max_depth = max_depth, max_features=max_features, criterion='mae', random_state=0)
regressor_sj.fit(features_sj, labels_sj)

# Prediction
pred_sj = [int(round(x)) for x in regressor_sj.predict(data_features_test_sj[features_selected_sj])]
data_features_test_sj = data_features_test_sj.assign(total_cases = pred_sj)


## Iquitos
data_features_test_iq = data_features_test.loc[data_features_test['city'] == 'iq']

# Normalization of the data
max_abs_scaler = preprocessing.MaxAbsScaler()
data_features_test_iq_norm = max_abs_scaler.fit_transform(data_features_test_iq[features_selected_iq])
features_iq_norm = max_abs_scaler.fit_transform(features_iq)

# Parametrization
n_neighbors = 18
weights = 'distance'

# Knn regressor
regressor_iq = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
regressor_iq.fit(features_iq, labels_iq)

# Prediction
pred_iq = [int(round(x)) for x in regressor_iq.predict(data_features_test_iq_norm)]
data_features_test_iq = data_features_test_iq.assign(total_cases = pred_iq)



### 5. Save results
result = data_features_test_sj.append(data_features_test_iq, ignore_index=True)
result = result[['city', 'year', 'weekofyear', 'total_cases']]
result.to_csv('./results.csv', index=False)
