# -*- coding: utf-8 -*-
"""
Created on Thu Nov 2 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero 
López-Sepúlveda
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### 1. Load the data asigned
try:
    data_features = pd.read_csv('../Data/dengue_features_train.csv')
    data_labels = pd.read_csv('../Data/dengue_labels_train.csv')
    
    data_features = data_features.head(347)
    data_labels = data_labels.head(347)
    
    data_features = data_features.fillna(0)
    data_labels = data_labels.fillna(0)
    
except:
    print("Error while loading the data")
    sys.exit()
    
    
    
    
# Remove outliers 87, 139
data_features = data_features.drop([87,139])
data_labels = data_labels.drop([87,139])

    
# Correlation between features and total cases    
from scipy.stats.stats import pearsonr 
corr = [pearsonr(data_features['ndvi_ne'], data_labels['total_cases'])[0],
        pearsonr(data_features['ndvi_nw'], data_labels['total_cases'])[0],
        pearsonr(data_features['ndvi_se'], data_labels['total_cases'])[0],
        pearsonr(data_features['ndvi_sw'], data_labels['total_cases'])[0],
        pearsonr(data_features['precipitation_amt_mm'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_air_temp_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_avg_temp_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_dew_point_temp_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_max_air_temp_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_min_air_temp_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_precip_amt_kg_per_m2'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_relative_humidity_percent'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_sat_precip_amt_mm'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_specific_humidity_g_per_kg'], data_labels['total_cases'])[0],
        pearsonr(data_features['reanalysis_tdtr_k'], data_labels['total_cases'])[0],
        pearsonr(data_features['station_avg_temp_c'], data_labels['total_cases'])[0],
        pearsonr(data_features['station_diur_temp_rng_c'], data_labels['total_cases'])[0],
        pearsonr(data_features['station_max_temp_c'], data_labels['total_cases'])[0],
        pearsonr(data_features['station_min_temp_c'], data_labels['total_cases'])[0],
        pearsonr(data_features['station_precip_mm'], data_labels['total_cases'])[0]]




features_names = ('ndvi_ne', 'ndvi_nw', 'ndvi_se', 'ndvi_sw', 'precipitation_amt_mm',
                  'reanalysis_air_temp_k', 'reanalysis_avg_temp_k', 'reanalysis_dew_point_temp_k',
                  'reanalysis_max_air_temp_k', 'reanalysis_min_air_temp_k', 'reanalysis_precip_amt_kg_per_m2',
                  'reanalysis_relative_humidity_percent', 'reanalysis_sat_precip_amt_mm',
                  'reanalysis_specific_humidity_g_per_kg', 'reanalysis_tdtr_k', 'station_avg_temp_c',
                  'station_diur_temp_rng_c', 'station_max_temp_c', 'station_min_temp_c', 'station_precip_mm')
y_pos = np.arange(len(features_names))
 
plt.bar(y_pos, corr, align='center', alpha=0.5)
plt.xticks(y_pos, features_names, rotation='vertical')
plt.ylabel('Correlation')
plt.title('Correlation features vs total cases')

plt.show()
