# Random-Forests - <sub></sub>
<sub>Random Forest is a popular ensemble learning algorithm used in machine learning for both classification and regression tasks. It operates by constructing a multitude of decision trees during training and outputting the mode (classification) or mean prediction (regression) of the individual trees.</sub>

Here's how Random Forest works:

- <sub><b>Bootstrapping:</b> Random Forest builds multiple decision trees by sampling the training data with replacement (bootstrapping). Each tree is trained on a different subset of the original dataset.</sub>
- <sub><b>Random Feature Selection:</b> During the construction of each decision tree, a random subset of features is selected at each node. This process helps in decorrelating the trees and reducing the chance of overfitting.</sub>
- <sub><b>Decision Tree Construction:</b> Each decision tree is grown to its maximum depth or until it reaches a minimum number of samples in each leaf node. At each node, the best split is chosen among a random subset of features, typically using metrics like Gini impurity or entropy for classification and mean squared error for regression.Here in this case we will focus more on Entropy</sub>
- <sub><b>Voting or Averaging:</b> For classification tasks, the predictions of individual trees are combined through a majority voting mechanism. For regression tasks, the predictions are averaged to obtain the final prediction.</sub>

Random Forest offers several advantages:

- <sub><b>High Accuracy:</b> Random Forest typically produces highly accurate predictions due to the aggregation of multiple decision trees.</sub>
- <sub><b>Robustness to Overfitting:</b> By aggregating predictions from multiple trees, Random Forest is less prone to overfitting compared to individual decision trees.</sub>
  - <sub>Overfitting : Overfitting doesn't necessarily mean the model achieves 100% accuracy. Instead, it refers to a situation where the model learns the training data too well, capturing noise or random fluctuations that aren't representative of the underlying pattern. This often leads to a model that performs poorly on new, unseen data despite having high accuracy on the training data.</sub>
  - <sub>Underfitting: Underfitting occurs when a machine learning model is too simple to capture the underlying structure of the data, resulting in poor performance on both the training and test data. </sub>

- <sub><b>Feature Importance:</b> Random Forest provides a measure of feature importance, indicating which features are most influential in making predictions.</sub>

<p align="center">
DATA PREPARATION FOR RANDOM FOREST <br/>
<sub>Data Preparation for Random Forest: In this case we are trying to Identify whether an Employee will Leave or Stay in the Firm.</sub>
<img src="https://i.imgur.com/CJeg6Rx.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<sub>Random Forest is widely used in various applications, including but not limited to, classification, regression, feature selection, and outlier detection. Its versatility, robustness, and ease of use make it a popular choice for both beginners and experienced practitioners in the field of machine learning.</sub>

Ensemble

<sub>Multiple Models: Ensemble methods create several individual models, each trained on different subsets of the data or using different algorithms.

<sub>Combining Predictions: Once the individual models are trained, their predictions are combined in some way to make a final prediction. This can be done by averaging the predictions, taking a vote among the models, or using more sophisticated techniques.

<sub>Improved Performance: By combining the predictions of multiple models, ensemble methods aim to reduce the risk of overfitting and improve generalization performance. Each model may capture different aspects of the data or make different errors, and combining them can lead to better overall performance.</sub>

Common ensemble techniques include

<sub><b>Bagging (Bootstrap Aggregating):</b> In bagging, multiple models are trained on different bootstrap samples of the data (random samples with replacement), and their predictions are averaged to make the final prediction. Random Forest is an example of a bagging ensemble method.

<sub><b>Boosting:</b> Boosting works by sequentially training multiple weak learners (models that perform slightly better than random chance) and focusing on the instances that are misclassified by previous models. Gradient Boosting Machines (GBMs) and AdaBoost are popular boosting algorithms.

<sub><b>Voting:</b> In voting ensembles, multiple models (e.g., decision trees, logistic regression, support vector machines) make predictions independently, and the final prediction is determined by a majority vote or by averaging the predictions.


<p align="center">
Using Ensemble from SKLEARN <br/>
<img src="https://i.imgur.com/LUvmVLs.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<p align="center">
Applying Gridserach on hyperparameter n_estimators (Number of Forests)<br/>
<img src="https://i.imgur.com/DB8KGFH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<p align="center">
Using the best number of Forests identify the Best Features and then retrain the model using Best Features:<br/>
<img src="https://i.imgur.com/nhzkEGc.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<p align="center">
Using Best Features and Again iterating for Best number of forests.:<br/>
<img src="https://i.imgur.com/DF4piwC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

<p align="center">
The Results:<br/>
<img src="https://i.imgur.com/6Zci372.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />

The Conclusion:

<sub> In the case we are studying, we want to measures the proportion of actual positive instances (e.g., positive class) that are correctly identified by the classifier. Here the positive class is "Whether the Employee will Stay with the Company" we want to identify this more correctly. Hence we use Recall. In simpler terms, recall answers the question: "Out of all the positive instances in the dataset, how many did the model correctly identify as positive?" A high recall indicates that the model is effective at capturing most of the positive instances in the dataset.

<sub> In our case, recall is 95.62% which means the model is predicting 95.6% more positive class. And reduce the false negative - Model incorrectly predicts that an employee will stay, but the employee actually leaves.




