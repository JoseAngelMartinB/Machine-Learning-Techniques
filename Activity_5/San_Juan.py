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
from scipy import cluster


### 0. Load the data asigned
try:
    data_features = pd.read_csv('../Data/dengue_features_train.csv')
    data_labels = pd.read_csv('../Data/dengue_labels_train.csv')
    data = pd.merge(data_features, data_labels, on=['city', 'year', 'weekofyear'])

    # Select the data from San Juan
    data = data.loc[data['city'] == 'sj']

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
plt.xlim(-0.5, 3.5)
plt.ylim(-1, 1.5)
ax.grid(True)
fig.tight_layout()
plt.show()

# Remove outliers
outliers = [89, 141, 401, 453, 713, 765]
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


### 4. Feature selection
