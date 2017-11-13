#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu 9 Nov 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero
López-Sepúlveda
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

from sklearn import preprocessing, decomposition
from sklearn.tree import DecisionTreeRegressor
from scipy import cluster
from scipy.stats.stats import pearsonr
from tabulate import tabulate


### 0. Load the data asigned
try:
    data_features = pd.read_csv('../Data/dengue_features_train.csv')
    data_labels = pd.read_csv('../Data/dengue_labels_train.csv')
    data = pd.merge(data_features, data_labels, on=['city', 'year', 'weekofyear'])

    # Select the data from San Juan
    data = data.loc[data['city'] == 'iq'].reset_index(drop=True)

    data = data.fillna(0)
    data_ini = data.drop(['city','year','weekofyear','week_start_date','total_cases'], 1)

except:
    print("Error while loading the data.")
    sys.exit()



### 1. Identify outliers

# Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
cases = min_max_scaler.fit_transform(data_ini)

# PCA Estimation
estimator = decomposition.PCA(n_components = 2)
X_pca = estimator.fit_transform(cases)
print("Percentage of variance explained by each of the selected components:")
print(estimator.explained_variance_ratio_)

# Plot
numbers = np.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i] + 2) # Because element index is element - 2
plt.xlim(-0.75, 3)
plt.ylim(-1, 1)
ax.grid(True)
fig.tight_layout()
plt.show()

# Remove outliers
outliers = [184, 236, 444, 496]
data = data.drop([x - 2 for x in outliers]) # Because element index is element - 2
data_ini = data_ini.drop([x - 2 for x in outliers]) # Because element index is element - 2



### 2. Hierarchical clustering algorithm using features as elements

# Normalization of the data
norm_data_ini_features = min_max_scaler.fit_transform(np.transpose(data_ini))

# Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim_ini_features = dist.pairwise(norm_data_ini_features)

# Building the Dendrogram
cut_threshold = 9
features_label_lst = list(data_ini.columns.values)
features_label = np.asarray(features_label_lst)

clusters_features = cluster.hierarchy.linkage(matsim_ini_features, method = 'complete')
cluster.hierarchy.dendrogram(clusters_features, color_threshold = cut_threshold, labels = features_label, leaf_rotation=90)
plt.subplots_adjust(top=0.95, bottom=0.45)
plt.show()



### 3. Correlation between features and total cases

features_names = ('ndvi_ne', 'ndvi_nw', 'ndvi_se', 'ndvi_sw', 'precipitation_amt_mm',
                  'reanalysis_air_temp_k', 'reanalysis_avg_temp_k', 'reanalysis_dew_point_temp_k',
                  'reanalysis_max_air_temp_k', 'reanalysis_min_air_temp_k', 'reanalysis_precip_amt_kg_per_m2',
                  'reanalysis_relative_humidity_percent', 'reanalysis_sat_precip_amt_mm',
                  'reanalysis_specific_humidity_g_per_kg', 'reanalysis_tdtr_k', 'station_avg_temp_c',
                  'station_diur_temp_rng_c', 'station_max_temp_c', 'station_min_temp_c', 'station_precip_mm')

corr = []
for elm in features_names:
    corr.append(pearsonr(data[elm], data['total_cases'])[0])

y_pos = np.arange(len(features_names))
plt.bar(y_pos, corr, align='center', alpha=0.5)
plt.xticks(y_pos, features_names, rotation='vertical')
plt.ylabel('Correlation')
plt.title('Correlation features vs total cases - Iquitos')
plt.subplots_adjust(top=0.95, bottom=0.45)
plt.show()

print("\nCorrelation between features and total cases:")
for i in range(0, len(features_names)):
    print("\t{0:38s} ==> {1:8f}".format(features_names[i], corr[i]))

#Density Plots
data_density = data.drop(['city', 'year', 'weekofyear', 'week_start_date', 'total_cases'], 1)
data_density.plot(kind='density', subplots=True, layout=(5,4), sharex=False)
plt.subplots_adjust(top=0.95, bottom=0.05, left=0.05, right=0.95)
plt.show()



### 4. Feature selection

# First feature selection
features_names = ['year', 'weekofyear',
                  'reanalysis_dew_point_temp_k', 'reanalysis_min_air_temp_k',
                  'station_diur_temp_rng_c', 'reanalysis_tdtr_k',
                  'reanalysis_specific_humidity_g_per_kg', 'station_avg_temp_c',
                  'reanalysis_relative_humidity_percent',
                  'precipitation_amt_mm', 'reanalysis_precip_amt_kg_per_m2']
features = data[features_names]
labels = data['total_cases']

# Cross validation analysis
from sklearn.model_selection import cross_val_score
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

# Print features relevancies
print 'Feature Relevancies'
regressor = DecisionTreeRegressor(criterion='mse', max_depth=3, random_state=0)
regressor.fit(features, labels)
list1 = zip(features, regressor.feature_importances_)
print tabulate(list1, headers=['Feature', 'Relevance'])

# Second feature selection
features_names = ['year', 'weekofyear',
                  'reanalysis_min_air_temp_k',
                  'reanalysis_tdtr_k',
                  'station_avg_temp_c',
                  'reanalysis_relative_humidity_percent',
                  'reanalysis_precip_amt_kg_per_m2']

features = data[features_names]
labels = data['total_cases']