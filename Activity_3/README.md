# Activity 3. Principal Component Analysis

## 1. Load and normalize the data assigned
Observing the data file, we have decided to obtain the necessary data from it 
without changing the original file. A filter is going to be used in order to 
obtain the data corresponding to San Juan city between January 1990 and January
1996.

The first 4 columns of the data file are only used for identifying the different
data records, therefore, they have not been used as features. Some rows do not
include all the data, consequently, a zero value has been inserted in that 
features. This rows has been removed. For that reason, the total number of elements
in the data set 345. Then, the data has been normalize using 
the MinMaxScaler of skylearn preprocessing package.


## 2. Find the best value for k
It has been calculated the silhouette coefficient. This coefficient is 1 in highly dense clustering, -1 in incorrect clustering and similar to zero when there is overlapping. Following this criteria we have chosen k as 2, because the silhouette coefficient takes the maximum value. 


## 3. Execute K-means
We have selected random points method to choose the initial centroids. The data used by the k-means algorithm is the one that has been normalized. After that, the data has been plotted using plotdata function. The points are plotted after executing the PCA, in order to visualize them in two dimensions.

Two clusters has been created whose main differences are:
Temperatures:  Are slightly bigger in the cluster 2.
Precipitations: There is a significant difference between both clusters, being much higher in the cluster 2. 


## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
