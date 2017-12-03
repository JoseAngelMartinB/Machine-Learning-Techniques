#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri 24 Nov 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero
López-Sepúlveda
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import neighbors
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn import preprocessing
from tabulate import tabulate



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



### 4. Back-Testing

# Split the data into a train subset and a test subset
bt_train_samples_sj = 800
bt_train_samples_iq = 400

n_elm_sj = data.loc[(data['city'] == 'sj')].shape[0]
n_elm_iq = data.loc[(data['city'] == 'iq')].shape[0]

bt_train_subset_sj = data.loc[(data['city'] == 'sj')].head(bt_train_samples_sj)
bt_train_subset_iq = data.loc[(data['city'] == 'iq')].head(bt_train_samples_iq)
bt_test_subset_sj = data.loc[(data['city'] == 'sj')].tail(n_elm_sj - bt_train_samples_sj)
bt_test_subset_iq = data.loc[(data['city'] == 'iq')].tail(n_elm_iq - bt_train_samples_iq)

bt_train_features_sj = bt_train_subset_sj[features_selected_sj]
bt_train_features_iq = bt_train_subset_iq[features_selected_iq]
bt_train_labels_sj = bt_train_subset_sj['total_cases']
bt_train_labels_iq = bt_train_subset_iq['total_cases']
bt_test_sj = bt_test_subset_sj[features_selected_sj]
bt_test_iq = bt_test_subset_iq[features_selected_iq]
bt_test_labels_sj = bt_test_subset_sj['total_cases']
bt_test_labels_iq = bt_test_subset_iq['total_cases']


## San Juan

'''
# Normalization of the data
min_max_scaler = preprocessing.MaxAbsScaler()
bt_train_features_sj = min_max_scaler.fit_transform(bt_train_features_sj)
bt_test_sj = min_max_scaler.fit_transform(bt_test_sj)
'''

# Random Forest
n_estimators = 50
max_depth = None
max_features = len(features_selected_sj)

regressor_sj = RandomForestRegressor(n_estimators= n_estimators, max_depth = max_depth, max_features=max_features, criterion='mae', random_state=0)
regressor_sj.fit(bt_train_features_sj, bt_train_labels_sj)

print 'Feature Relevancies San Juan'
list1 = zip(features_selected_sj, regressor_sj.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

'''
# Other methods used to compete:

# Knn
n_neighbors = 51
weights = 'uniform'

regressor = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
regressor.fit(bt_train_features_sj, bt_train_labels_sj)


# AdaBoost
regressor = AdaBoostRegressor(n_estimators=50)
regressor.fit(bt_train_features_sj, bt_train_labels_sj)


# Gradient Boost
regressor_sj = GradientBoostingRegressor(loss='huber', learning_rate=0.1, n_estimators=100, max_depth=None, criterion='friedman_mse')
regressor_sj.fit(bt_train_features_sj, bt_train_labels_sj)
'''

bt_pred_sj = [int(round(x)) for x in regressor_sj.predict(bt_test_sj)]


## Iquitos

# Normalization of the data
min_max_scaler = preprocessing.MaxAbsScaler()
bt_train_features_iq = min_max_scaler.fit_transform(bt_train_features_iq)
bt_test_iq = min_max_scaler.fit_transform(bt_test_iq)

# Knn
n_neighbors = 18
weights = 'distance'

regressor_iq = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights, p=2)
regressor_iq.fit(bt_train_features_iq, bt_train_labels_iq)

'''
# Other methods used to compete:

# AdaBoost
regressor = AdaBoostRegressor(n_estimators=50)
regressor.fit(bt_train_features_iq, bt_train_labels_iq)


# Random Forest
n_estimators = 50
max_depth = None
max_features = len(features_selected_iq)

regressor_iq = RandomForestRegressor(n_estimators= n_estimators, max_depth = max_depth, max_features=max_features, criterion='mae', random_state=0)
regressor_iq.fit(bt_train_features_iq, bt_train_labels_iq)

print 'Feature Relevancies Iquitos'
list2 = zip(features_selected_iq, regressor_iq.feature_importances_)
print tabulate(list2, headers=['Feature', 'Relevance'])
'''

bt_pred_iq = [int(round(x)) for x in regressor_iq.predict(bt_test_iq)]


## MAE (Mean absolute error)
print("\nBack-Testing - MAE (Mean absolute error):")

mae = mean_absolute_error(bt_test_labels_sj.values.tolist(), bt_pred_sj)
print("\t- San Juan - MAE: %.4f" % mae)

mae = mean_absolute_error(bt_test_labels_iq.values.tolist(), bt_pred_iq)
print("\t- Iquitos  - MAE: %.4f" % mae)

bt_true_labels = bt_test_labels_sj.values.tolist() + bt_test_labels_iq.values.tolist()
bt_pred_labels = bt_pred_sj + bt_pred_iq
mae = mean_absolute_error(bt_true_labels, bt_pred_labels)
print("\tTotal MAE: %.4f" % mae)


## Print prediction plot
figs, axes = plt.subplots(nrows=2, ncols=1)
plt.tight_layout(h_pad=2.5)
plt.subplots_adjust(top=0.85, bottom=0.15)

# Plot San Juan
axes[0].set_title("San Juan")
data_sj_plt = data.loc[(data['city'] == 'sj')]
data_sj_plt = data_sj_plt.assign(pred = regressor_sj.predict(data_sj_plt[features_selected_sj]))
data_sj_plt.pred.plot(x=('year','weekofyear'), ax=axes[0], label="Predictions")
data_sj_plt.total_cases.plot(ax=axes[0], label="Actual")

# Plot Iquitos
axes[1].set_title("Iquitos")
data_iq_plt = data.loc[(data['city'] == 'iq')]
data_iq_plt = data_iq_plt.assign(pred = regressor_iq.predict(min_max_scaler.fit_transform(data_iq_plt[features_selected_iq])))
data_iq_plt.pred.plot(ax=axes[1], label="Predictions")
data_iq_plt.total_cases.plot(ax=axes[1], label="Actual")

plt.suptitle("Predicted Cases vs. Actual Cases")
plt.legend()
plt.show()