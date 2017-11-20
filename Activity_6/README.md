# Activity 6. Predictive Model Building
At this point of development, it is time to start predicting. In the previous activities we have developed a data analysis work to see how the data is grouped and related together. Moreover, we have carried out a selection of features, according to the criteria we have considered most appropriate. Now, a first prediction is going to be carried out using the k-nearest neighbors regression algorithm.


## Missing Values
The first thing to consider is what values ​​of our dataset are useful. Therefore, if we look at the data it can shown how some rows have incomplete data or even are empty (without any record in any feature). With this information, we have decided to do an interpolation of the data in order to guess the values of the empty fields. Hence, a better approximation to the real data will be achieved. Also, this will allow us to carry out a better analysis and, consequently, a better final prediction.

At his point we have to remember that, as it was stated in previous activities, we have some outliers corresponding to data elements with lot of empty features values (because we fill the empty data with zeros). Now, as we have applied an interpolation to fill these empty values, we are not going to have outliers. Nevertheless, to avoid having a bad analysis, since outliers will contain fictitious data obtained through interpolation (it does not reflect the reality) we are going to eliminate them.


## Feature Selection
The selection of features is the same as we have chosen in ![activity 5](../Activity_5), so there is no modification in this activity.


## Parametrization
Once we have cleaned the data and the features has been reduced, is time to start the parametrization of the KNN regression model. We have decided not to normalize the data, because tests using MinMaxScaler have shown that the cross-validation (CV) value is lower without normalization. This can means that the features chosen for the KNN are not relevant enough or that another normalization technique should be used.

The cross validation analysis has been performed with 2 values for the weight scheme (uniform and distance). A slightly better result has been observed using the uniform weight scheme in San Juan and also in Iquitos. Therefore, the number of neighbors (k) that will be selected for San Juan is 10.

![sanJuan cv scores](images/sanJuan_cv_scores.png)

On the other hand, in the case of Iquitos, we have considered 18 as a good value for the number of neighbors.

![iquitos cv scores](images/iquitos_cv_scores.png)


## Execute KNN and make predictions
Once the parameters for the KNN algorithm are known for both cities, we can start making predictions using the test dataset. Predictions will be carried out separately for each city and later it will be joined in a final csv, which is called results.csv. The results of the predictions should be given as integers for the competition, therefore, they will be rounded.



## Participating in the competition
Once the predictions are obtained and stored in the corresponding csv file, we are ready to start participating in the competition. After uploading the file to the driven-data [competition](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/) this was our score:

![dengAI score](images/dengAI_score.png)

## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
