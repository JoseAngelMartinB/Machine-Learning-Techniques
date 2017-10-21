# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:30:21 2017

@author: José Ángel Martín Baos, Oscar Pérez Galán, Miguel Ampuero 
López-Sepúlveda
"""

import codecs
import time
import sys
import numpy as np
from numpy import corrcoef, transpose, arange
from pylab import pcolor, show, colorbar, xticks, yticks

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn import preprocessing 

### 1. Load the data asigned
try:
    f = codecs.open("../Data/dengue_features_train.csv", "r", "utf-8")
    cases = []
    count = 0
    for line in f:
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
    
    
### 2. Extract the correlation among features
# plotting the correlation matrix
R = corrcoef(transpose(cases))
pcolor(R)
colorbar()
yticks(arange(0,20),range(0,20))
xticks(arange(0,20),range(0,20))
show()

# Generate a mask for the upper triangle
sns.set(style="white")
mask = np.zeros_like(R, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(200, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(R, mask=mask, cmap=cmap, vmax=.8,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)


### 3. Execute PCA and plot the results
#Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
cases = min_max_scaler.fit_transform(cases)
       
#PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(cases)

print(estimator.explained_variance_ratio_) 

#Plot 
numbers = np.arange(len(X_pca))
fig, ax = plt.subplots()
for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], numbers[i] + 2) # + 2 para que coincida con la línea del fichero
plt.xlim(-0.65, 0.4)
plt.ylim(-0.75, 1)
ax.grid(True)
fig.tight_layout()
plt.show()
