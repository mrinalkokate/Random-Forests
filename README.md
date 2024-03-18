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
