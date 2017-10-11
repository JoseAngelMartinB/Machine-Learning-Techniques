# Activity 1. Principal Component Analysis

## 1. Load and normalize the data asigned
Observing the data file, we have decided to obtain the necesarry data from it 
without changing the original file. A filter is going to be used in order to 
obtain the data correspondig to San Juan city between January 1990 and January
1996.

The first 4 coloums of the data file are only used for identifying the direfent
data records, therefore, they have not been used as features. Some rows do not
include all the data, consecuently, a zero value has been inserted in that 
features.Then, the data has been normelize using the MinMaxScaler of skylear 
preprocessing package.

Futhermore, the first line of the data file is the one containing the labels of 
the different features, and it has been stored in order to use them in part 4.


## 2. Compute the similarity matrix and execute the hierarchical clustering algorithm
This task has been developed in [activity_2.py](activity_2.py). Here the similarity 
matrix has been computed using the euclidean metric. This allow us to obtain the
distance between all the elments.

The next step is to build the dendrogram. We are using an agglomerative clustering
approach. First, it is needed to compute the distances between the most similar members 
for each pair of clusters (linkage). Therefore, three approaches can be used: single, complete and
average linkage. We have decided to use complete linkage because the single one are 
sensible to outliers, and our date has some of them, so the result is not descriptive.


## 3. Cut the dendogram and characterize the obtained groups
After generating the dendrogram, we have determine the cut of the dendrogram to 5. Therefore, 
we have obtained 14 clusters. The mean values of the different features in each cluster
has been computed and can be shown in [results.csv](results.csv) (do not forget to
select semicolon as separator when importing the data in Excel).

Some of these clusters are very similar. Hence, we are going to group some of these clusters
into bigger clusters. The final cluster list is:
* Cluster A (Group 1): Outliers that only have data from the Satellite vegetation.
* Cluster B (Group 2 and 3): They form a group because they have some features very similar
such as ndvi\_ne, ndvi\_nw, ndvi\_se and ndvi\_sw.
* Cluster C (Group 4, 5 and 6): They are related because of some features such as: ndvi\_se,
ndvi\_sw.
* Cluster D (Group 7, 8, 9, 10 and 11): Nothing relevant has been found. 
* Cluster E (Group 12, 13, 14): This cluster is very different to the other ones because they
have high precipitation values.


## 4. Execute the hierarchical clustering algorithm using feature as elements
In order to carry out this task, [clustering_features.py](clustering_features.py)
has been developed. 

We can visualize 5 different clusters on the image (numbered 1-5 from left to right). Before talking about each cluster, it is remarkable that the 4 and the 5 cluster has more relation between them in comparison to the others clusters. 
Also it is remarkable how there are two different clusters (on the opposite part of the graph) that both of them measures temperatures. One of the main reasons that this can occur is becuase the number one is measured in kelvin and the cluster number 5 is measured in celsius degrees. 

The cluster 3 makes sense becuase all the precipitacion data is gathered. Another remarkable aspect is that the relative humidity feature is isolated, it is alone in the second cluster. Finally, the Satellite veggetation is gathered in one cluster (the number four). 
