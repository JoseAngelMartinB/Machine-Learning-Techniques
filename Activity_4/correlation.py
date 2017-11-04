#!/usr/bin/env python2
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
from scipy.stats.stats import pearsonr


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

    
### 2. Correlation between features and total cases
corr = [pearsonr(data['ndvi_ne'], data['total_cases'])[0],
        pearsonr(data['ndvi_nw'], data['total_cases'])[0],
        pearsonr(data['ndvi_se'], data['total_cases'])[0],
        pearsonr(data['ndvi_sw'], data['total_cases'])[0],
        pearsonr(data['precipitation_amt_mm'], data['total_cases'])[0],
        pearsonr(data['reanalysis_air_temp_k'], data['total_cases'])[0],
        pearsonr(data['reanalysis_avg_temp_k'], data['total_cases'])[0],
        pearsonr(data['reanalysis_dew_point_temp_k'], data['total_cases'])[0],
        pearsonr(data['reanalysis_max_air_temp_k'], data['total_cases'])[0],
        pearsonr(data['reanalysis_min_air_temp_k'], data['total_cases'])[0],
        pearsonr(data['reanalysis_precip_amt_kg_per_m2'], data['total_cases'])[0],
        pearsonr(data['reanalysis_relative_humidity_percent'], data['total_cases'])[0],
        pearsonr(data['reanalysis_sat_precip_amt_mm'], data['total_cases'])[0],
        pearsonr(data['reanalysis_specific_humidity_g_per_kg'], data['total_cases'])[0],
        pearsonr(data['reanalysis_tdtr_k'], data['total_cases'])[0],
        pearsonr(data['station_avg_temp_c'], data['total_cases'])[0],
        pearsonr(data['station_diur_temp_rng_c'], data['total_cases'])[0],
        pearsonr(data['station_max_temp_c'], data['total_cases'])[0],
        pearsonr(data['station_min_temp_c'], data['total_cases'])[0],
        pearsonr(data['station_precip_mm'], data['total_cases'])[0]]

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


#Density Plots
data_density = data.drop(['city', 'year', 'weekofyear', 'week_start_date'], axis=1, inplace=True)
data.plot(kind='density', subplots=True, layout=(6,4), sharex=False)
plt.show()

