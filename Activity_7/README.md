# Activity 7. Submission

# Improving Predictions
This will be our final part of the project, as we have seen in previous activities we have made a series of studies on the data and algorithms that allow us to choose the best ways to make our predictions as correct as possible.

In this last activity we will carry out improvements on what is known so far, we will also discuss new approaches that help us with these improvements


# Back-Testing 

# Decisions in the data

# Others Algorithms

# New selection of features
As we said, we are going to try to improve our results, so it is necessary to see where the prediction problems are, one of the most important is the study and selection of the features.

If we observe the set of features we obtained in activity 6, we observe that the number of fatures is quite high, this can be a problem since the less relevant features could generate noise in the study of the set of features. For this reason we have taken the decision to leave a single representative for each cluster, the criterion for selecting the feature is to choose the feature with greater relevance within each subset, so that we would obtain the next selection of features.

![New Selection Features](images/NewFeaturesSelection.png)

This new set of features more reduced should be able to eliminate the problem we had of noise between features, and help us improve with our predictions

# Last years to make predict
This approach raises the problem that we should not work with the whole set of data, since the number of cases tends to be very different from the first years, this is a problem and as with the features these early years can also generate noise for our predictions.

![Last Yeras Selection](images/LastYears.png)

In order to make a decision when establishing a cut, arbitrary for the moment, when we perform the back-testing we will verify which cut is better for the data,that once done, we obtain a cut value of 650 for San Juan and 300 for Iquitos.

# Training and predicting
After the successive modifications applied to the set of data, we have to train and make predictions, but we are also going to make some changes in this section, the first one will change the classifier for the San Juan data set, choosing for it the Random Forest, since after tests on the obtained results we have seen that this type of classifier provides better results.

In the tests we have determined that the best number of estimators for our data is 50, if we increase this value it would surely improve the prediction, but it would do so minimally and since we have established a depth of None, then this would cause a consumption of memory too high, the depth has the value None since we let the algorithm have overfitting, which for the San Juan values cause a better result.

In the case of Iquitos, it will remain the same as activity 6, except that now we carry out a normalization on the data, this normalization we believe it necessary since we have data of different measurement scales, therefore, we will do the normalization with MaxAbsScaler,and to applying a transform to the data to avoid dispersion.

we will also modify the weight parameter by "distance", which is the one with which we obtained a better result.

# New submissions results
Now we just have to save the predictions made on a .csv file and submit the competition to see our new score and see if we really have improved.
![Results Submission](images/Results.png)

## Authors
* José Ángel Martín Baos
* Oscar Pérez Galán
* Miguel Ampuero López-Sepúlveda
