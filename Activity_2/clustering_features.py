# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:30:21 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero 
López-Sepúlveda
"""

import codecs
import sys
import numpy
import matplotlib.pyplot as plt

from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
from sklearn.decomposition import PCA


### 1. Load the data asigned
try:
    f = codecs.open("../Data/dengue_features_train.csv", "r", "utf-8")
    cases = []
    features_label = []
    count = 0
    for line in f:
        if count == 0:
            row = line.split(",")
            for i in range(4,len(row)):
                features_label.append(row[i])
        if count > 0: 
            # Insert a 0 in unfilled fields
            while ",," in line:
                line = line.replace(',,', ',0,')
            line = line.replace(',\n', ',0')
            
            row = line.split(",")
            if row[0] == "sj":
                if int(row[1])>=1990 and int(row[1])<=1996:
                    if row != []:
                        row = row[4:]
                        cases.append(map(float, row))
        count += 1
    f.close()
except:
    print("Error while loading the data")
    sys.exit()

cases = numpy.transpose(cases);
    

### 2. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)


### 3. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(norm_cases)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Average Distance', avSim)


### 4. Building the Dendrogram	
clusters = cluster.hierarchy.linkage(matsim, method = 'complete')
cluster.hierarchy.dendrogram(clusters, color_threshold = 7, labels = features_label, leaf_rotation=90)
plt.show()

