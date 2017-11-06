# Activity 4. Decision Trees for Regression

## 1. Correlation between features and total cases.
For the study of the correlation between the features and the total cases we used the Pearson correlation coefficient which allows us to know the existing linear relationship between the different features with the total cases. Following this way we will obtain a global vision of how the features are related (remember that a low relation does not imply that these features are not influential for the prediction, only that they are not related in a linear way).

In our case it can be observed how some features present a high correlation, the strongest being the features provided by the vegetationsatellite data, there are also quite weak relationships in the case of reanalysis_precip_amt_kg_per_m2 or
reanalysis_relative_humidity_percent which indicates that there is no direct relationship between features and total cases.

![Correlations](images/correlation.png)

## 2. Feature Selection
This is the most critical part, since it will depend on it if our model is able to achieve more accurate predictions.

In order to decide which features will be removed first, we must use some graphics that provide us knowledge of how our data are distributed. To study the data we will be helped by density charts that provide us information that allows us to discard features with a similar distribution. In our case this is very well appreciated in the graphics of ndvi_ne, ndvi_nw, ndvi_se and ndvi_sw, from which we decided to eliminate all except ndvi_se and nvdi_sw. We have chosen this two because are the most representative from this type of features. As in the next iterations in the developing process of this project we will need to select some of them, the best approach right now is to have a pair of features  from each representative cluster that can be found in the Clustering features graph (generated in the ![Activity 2](../Activity_2)).  This feature also presents a greater correlation with the total cases, as it has been seen in the first graph of this file. From this image, it is remarkable how all the precipitations density graphs follows the same distribution as the total number of cases. For selecting the two best features of precipitations, we will use the Clustering features graph described in this section.

![Density_Plot](images/Density_Plot.png)

We must also have into account how our features are distributed in the clustering that we have just finished in the Activity 3. In this graph you can see how similar are the features and gives us extra information that will lead us to make choices of features. As it can be seen in the previous image, the precipitations has the same distribution as the total number of cases. With the clustering graph took us to conclusion that we should stay with reanalysis_sat_precip_amt_mm and station_precip_mm in  representation of precipitation feature.

The same that happened with the precipitation and vegetation, we have chosen  representatives in the temperatures ( reanalysis_max_air_temp_k, reanalysis_air_temp_k and  station_max_temp_c) and just one in humidity feature ( reanalysis_specific_humidity_g_per_kg).

![Clustering_features](images/clustering_features.png)


## 3. Build a Decision Tree Model
Through these mechanisms we will try to deduce together with the previously selected features, how accurate our prediction will be. For this, we must first create the decision tree indicating that in our case we want the criterion to be 'mse' (mean squared error), together with the depth that we will reach. To avoid overtraining our data and overfiting occurs we have to calculate, before we have to calculate the best value of max_depth for our data. For this we will need to carry out the cross-validation in order to avoid overfitting, what we do with this is to select subsets of our data and test it with another set of data to finally reach a representation of the best values for max_depth of way that as we can see in our case is 2 which is the lowest value.

![Cross_Validation](images/Cross_Validation.png)

Feature Relevancies

| Feature                               	| Relevance 	|
|---------------------------------------	|-----------	|
| year                                  	| 0         	|
| weekofyear                            	| 0.0593644 	|
| ndvi_se                               	| 0         	|
| ndvi_sw                               	| 0.806768  	|
| reanalysis_max_air_temp_k             	| 0         	|
| reanalysis_air_temp_k                 	| 0.133868  	|
| reanalysis_specific_humidity_g_per_kg 	| 0         	|
| station_max_temp_c                    	| 0         	|
| station_precip_mm                     	| 0         	|
| reanalysis_sat_precip_amt_mm          	| 0         	|

For the evaluation we have split the data into two subsets various times: train and test. With the results we have received from this evaluations we apply an average on the predictions giving as result the estimation of the error. As we just have mentioned in this document, our best max_depth value is 2.

## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
