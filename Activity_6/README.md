# Activity 6. Predictive Model Building
At this point of development, it is time to start predicting. Previously on this repository we have developed a data analysis work to see how they are grouped and related together with a selection of features, according to the criteria we have considered most appropriate.

## Missing Values
The first thing to consider is that values ​​of our data set are useful. Therefore, if we look at the data we can see how some of them have incomplete data or even are empty, without any record in any feature. With this information, we have decided that it can be really useful to do an interpolation of the data, getting no empty fields. Therefore we will get a better approximation to the reality of the data we are working on. Also, being able to carry out a better analysis and therefore a better final prediction.

At his point we have to remember that, as we saw, we had the outliers but now they have been completed with records. But some of the empty data corresponds to a set of dates that has less information. By consequence, this subset is calculated with less source data and it will be considered as outliers. To avoid having a bad analysis, since this subset is a fictitious data (it does not reflect the reality) we are going to eliminate them.



## Feature Selection
The selection of features is the same as we have chosen in ![activity 5](../Activity_5), so there is no modification in this README.



## Parametrization
Once we have the clear data and features, we must parameterize the data according to some criteria. For this occasion we have decided not to normalize the data, since by doing tests we have seen that the CV value is better without normalization. This means that the selection of features is not entirely correct.

The cross validation analysis is performed with 2 values for weights (uniform and distance), where we will use the Neighbors-based regression model. Once both weights are finished, we can see the CV values obtained. Observing a better result using uniform, as we see for the case of San Juan in which we see that the best CV value is reached when the number of neighbors is 35.
![sanJuan cv scores](images/sanJuan_cv_scores.png)

On the other hand, in the case of Iquitos, reaches its best CV when a neighbor value equals to 18.
![iquitos cv scores](images/iquitos_cv_scores.png)


## Execute kNN and make predictions
We already know the best number of neighbors for each case and the best weight. So we can start making predictions based on those values obtained previously. First of all we execute the KNN and we make the prediction of the features of each city with their corresponding labels.

The predictions will be rounded to avoid losing information and once it is completed, they will be saved in the file result.to_csv.

## Participating in the competition
Once the predictions are finished and we have obtained the result csv file, we are ready to start participating in the competition.
For being able to orient ourselves and consider possible modifications on our decisions, the team has decided to submit this resulting csv file.

After uploading the file to the driven-data [competition](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/) this was our score:
![dengAI score](images/dengAI_score.png)

## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
