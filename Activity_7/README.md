# Activity 7. Submission

# Improving Predictions
This will be our final part of the project, as we have seen in previous activities we have made a series of studies on the data and algorithms that allow us to choose the best ways to make our predictions as correct as possible.

In this last activity we will carry out improvements on what is known so far, we will also discuss new approaches that help us with these improvements


# Back-Testing 

In general terms, is the process of testing a strategy before implementing it. It allows us to know if the approach we are using is correct or not.  To accomplish this function we work with our local data. We have made a division in two subsets, one for training and other one for testing. The selection is proportional to the data we have from each city. That is the reason the subset of training is bigger in San Juan than Iquitos, due to we have more records of the first city. With this method we are able to predict our own data. Even we already know the accurate result, the goal of this section is to verify that our predictions are correct. 

With the algorithms used and trained in the back-testing, we have made a prediction over the whole dataset. The predicted results and the real dengue cases for San Juan and Iquitos can be shown in the following image.

![Predicted cases](images/Predicted_cases.png)


# New selection of features
As we said, we are going to try to improve our results, so it is necessary to see where the prediction problems are, one of the most important is the study and selection of the features.

If we observe the set of features we obtained in activity 6 for Iquitos, we observe that the number of fatures is quite high, this can be a problem since the less relevant features could generate noise in the study of the set of features. For this reason we have taken the decision to eliminate some features based on their relevance, so that even if some clusters are left without a representative feature, this is the way to reduce that noise, and therefore the improvement we were looking for.

![New Selection Features](images/NewFeaturesSelection.png)

One of the features that was in both sets has been the "year", this feature generates a high distortion in the data, and really is not a feature that helps predict better, therefore it has been eliminated from multiple sets of features.

This new set of features more reduced should be able to eliminate the problem we had of noise between features, and help us improve with our predictions

# Last years to make predict
This approach raises the problem that we should not work with the whole set of data, since the number of cases tends to be very different from the first years, this is a problem and as with the features these early years can also generate noise for our predictions.

![Last Yeras Selection](images/LastYears.png)

To solve this problem we make a selection of the last data of each set, which as we have seen in our tests, would be the last 650 data of San Juan and the last 300 of Iquitos.

This has been one of the key improvements to reduce the error when predicting, demonstrating that effectively the first data generate worse results and cause distortion.

# Algortihm changes
After the successive modifications applied to the set of data, we have to train and make predictions, but we are also going to make some changes in this section,depending on the city.

San Juan modifications:

The first one will change the classifier for the San Juan data set, choosing for it the Random Forest, since after tests on the obtained results we have seen that this type of classifier provides better results,in the tests we have determined that the best number of estimators for our data is 50, if we increase this value it would surely improve the prediction, but it would do so minimally and since we have established a depth of None, then this would cause a consumption of memory too high, the depth has the value None since we let the algorithm have overfitting, which for the San Juan values cause a better result.

Iquitos modifications:

In the case of Iquitos, it will remain the same as activity 6, except that now we carry out a normalization on the data, this normalization we believe it necessary since we have data of different measurement scales, therefore, we will do the normalization with MaxAbsScaler,and to applying a transform to the data to avoid dispersion.We will also modify the weight parameter by "distance", which is the one with which we obtained a better result.

# New submissions results
Now we just have to save the predictions made on a .csv file and submit the competition to see our new score and see if we really have improved.
![Results Submission](images/Results.png)

## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
