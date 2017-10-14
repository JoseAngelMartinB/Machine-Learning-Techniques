# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero 
López-Sepúlveda
"""

import codecs

import sys
import matplotlib.pyplot as plt
import numpy

from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def plotdata(data,labels,name): #def function plotdata
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()


### 1. Load the data asigned
try:
    f = codecs.open("../Data/dengue_features_train.csv", "r", "utf-8")
    cases = []
    count = 0
    for line in f:
        if count > 0 and count != 88 and count != 140: #remove outliers 87, 139
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


### 2. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
norm_cases = min_max_scaler.fit_transform(cases)

#PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(norm_cases)

print(estimator.explained_variance_ratio_)


### 3. Plot the data
labels = [0 for x in range(len(X_pca))]
plotdata(X_pca,labels,'basic')


### 4. Setting parameters
k = 4
init = "random"
iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 # random


### 5. Execute clustering 
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels = km.fit_predict(norm_cases)


### 6. Plot the results
plotdata(X_pca,labels, init)

