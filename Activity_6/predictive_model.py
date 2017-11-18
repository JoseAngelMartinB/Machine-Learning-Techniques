#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu 17 Nov 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero
López-Sepúlveda
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import neighbors
from sklearn.model_selection import cross_val_score



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
labels_sj = data.loc[data['city'] == 'sj']['total_cases']
labels_iq = data.loc[data['city'] == 'iq']['total_cases']



### 4. Parametrization

'''
- No normalization has been used.
- Distance function: euclidean distance.
- K value:
    San Juan = 10
    Iquitos  = 18
- Weight scheme: Uniform
'''

# Cross validation analysis - San Juan
for _,weights in enumerate(['uniform', 'distance']):
    tot_scores = []
    for n_neighbors in range(1,40):
        knn = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
        knn.fit(features_sj, labels_sj)
        # Scoring function: negative mean absolute error.  Number of folds: 10
        scores = -cross_val_score(knn, features_sj, labels_sj, scoring='neg_mean_absolute_error', cv=10)
        tot_scores.append(scores.mean())

    plt.plot(range(0, len(tot_scores)), tot_scores, marker='o', label=weights)
    plt.ylabel('cv score')

plt.title('San Juan - CV scores')
plt.legend()
plt.show()


# Cross validation analysis - Iquitos
for _,weights in enumerate(['uniform', 'distance']):
    tot_scores = []
    for n_neighbors in range(1,40):
        knn = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
        knn.fit(features_iq, labels_iq)
        # Scoring function: negative mean absolute error.  Number of folds: 10
        scores = -cross_val_score(knn, features_iq, labels_iq, scoring='neg_mean_absolute_error', cv=10)
        tot_scores.append(scores.mean())

    plt.plot(range(0, len(tot_scores)), tot_scores, marker='o', label=weights)
    plt.ylabel('cv score')

plt.title('Iquitos - CV scores')
plt.legend()
plt.show()



### 5. Execute kNN and make predictions

# San Juan
data_features_test_sj = data_features_test.loc[data_features_test['city'] == 'sj']

n_neighbors = 35
weights = 'uniform'

knn = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
knn.fit(features_sj, labels_sj)

pred_sj = [int(round(x)) for x in knn.predict(data_features_test_sj[features_selected_sj])]

data_features_test_sj = data_features_test_sj.assign(total_cases = pred_sj)


# Iquitos
data_features_test_iq = data_features_test.loc[data_features_test['city'] == 'iq']

n_neighbors = 18
weights = 'uniform'

knn = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
knn.fit(features_iq, labels_iq)

pred_iq = [int(round(x)) for x in knn.predict(data_features_test_iq[features_selected_iq])]

data_features_test_iq = data_features_test_iq.assign(total_cases = pred_iq)


# Save results
result = data_features_test_sj.append(data_features_test_iq, ignore_index=True)
result = result[['city', 'year', 'weekofyear', 'total_cases']]
result.to_csv('./results.csv', index=False)