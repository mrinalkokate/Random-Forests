# -*- coding: utf-8 -*-
"""RandomForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JNRzoOqZ7A_17XUf2Kp0uFF1JHf-MO_N
"""

# Data Preparation
from pandas import read_csv, get_dummies,Series
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
dataset=read_csv('/content/drive/MyDrive/Colab Notebooks/Emloyees.csv')# reading
dataset['PastEmployee'] = dataset['PastEmployee'].map({'Yes':0, 'No':1}) # encoding
dataset['OverTime'] = dataset['OverTime'].map({'Yes':1, 'No':0}) # encoding
dataset['Gender'] = dataset['Gender'].map({'Female':1, 'Male':0}) # encoding
data2 = get_dummies(dataset, columns =  ['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'MaritalStatus']) # encoding
X = data2.drop('PastEmployee', axis = 1) # Features
Y = data2['PastEmployee'] # Labels
X_scaled = StandardScaler().fit_transform(X) # scaling

X_train, X_test, Y_train, Y_test = train_test_split( X_scaled, Y, test_size = 0.3, random_state = 100)# splitting
X_train,Y_train =SMOTE (random_state = 100).fit_resample(X_train,Y_train)# balancing

# Random Forest Classifier (method 1)
#from sklearn.ensemble import RandomForestClassifier
from sklearn import ensemble
#RF_classifier1 =ensemble.RandomForestClassifier()
RF_classifier1 =ensemble.RandomForestClassifier(n_estimators=50, criterion='entropy', max_features='auto', random_state=1)  # building model
RF_classifier1.fit(X_train,Y_train)#training
Y_pred1=RF_classifier1.predict(X_test)# testing
# imp_features = Series(RF_classifier1.feature_importances_, index=list(X)).sort_values(ascending=False)
# print(imp_features)

# Evaluation
# Acuracy and confusion matrix
from sklearn import metrics
Accuracy=metrics.accuracy_score(Y_test, Y_pred1) # calculating accuaracy
print("Accuracy: ", Accuracy) # Is this a good metric??
con_matrix = metrics.confusion_matrix(Y_test, Y_pred1)
print (con_matrix)
recall = metrics.recall_score(Y_test, Y_pred1)
print (recall)
percision=metrics.precision_score(Y_test, Y_pred1)
print(percision)

# Random Forest Classifier (method 2)
from sklearn.model_selection import GridSearchCV
RF_classifier2 = ensemble.RandomForestClassifier(criterion='entropy', max_features='auto', random_state=1) # building model
no_trees = {'n_estimators': [200, 250, 300, 350, 400, 450]}
grid_search1 = GridSearchCV(estimator=RF_classifier2, param_grid=no_trees, scoring='recall', cv=5)
grid_search1.fit(X_scaled, Y)## training, testing , evaluation, ranking.
best_parameters = grid_search1.best_params_
print(best_parameters)
best_result = grid_search1.best_score_
print(best_result)

# Random Forest Classifier with best number of tree (method 1)

RF_classifier3 = ensemble.RandomForestClassifier(n_estimators=400, criterion='entropy', max_features='auto', random_state=1)# building model
RF_classifier3.fit(X_train,Y_train) #training
Y_pred3=RF_classifier3.predict(X_test)# testing
imp_features = Series(RF_classifier3.feature_importances_, index=list(X)).sort_values(ascending=False)
print(imp_features)

# Using important features only (method #2)
X2 = data2[['OverTime', 'Age', 'EnvironmentSatisfaction', 'MonthlyIncome', 'NumCompaniesWorked']]
X_scaled = StandardScaler().fit_transform(X2) # scaling
# X_train, X_test, Y_train, Y_test = train_test_split( X_scaled, Y, test_size = 0.3, random_state = 100)# splitting
# X_train,Y_train =SMOTE (random_state = 100).fit_resample(X_train,Y_train)# balancing

RF_classifier4 = ensemble.RandomForestClassifier(criterion='entropy', max_features='auto', random_state=1) # building classifier
no_trees = {'n_estimators': [200, 250, 300, 350, 400, 450]}
grid_search2 = GridSearchCV(estimator=RF_classifier4, param_grid=no_trees, scoring='recall', cv=5)
grid_search2.fit(X_scaled, Y) # training, testing , evaluation, ranking.

best_parameters = grid_search2.best_params_
print(best_parameters)
best_result = grid_search2.best_score_
print(best_result)

# Using pipeline (method #3)
from imblearn.pipeline import Pipeline
RF_classifier5 = Pipeline([('balancing', SMOTE(random_state = 101)),
        ('classification', ensemble.RandomForestClassifier(criterion='entropy', max_features='auto', random_state=1) )]) # building classifier
no_trees = {'classification__n_estimators': [10,20,30,40,50,100]}
grid_search3 = GridSearchCV(estimator=RF_classifier5, param_grid=no_trees, scoring='precision', cv=5)
grid_search3.fit(X_scaled, Y)

best_parameters = grid_search3.best_params_
print(best_parameters)
best_result = grid_search3.best_score_
print(best_result)

# Building random forest (method #1 ) with the best number of trees
RF_classifier6 = ensemble.RandomForestClassifier(n_estimators=20, criterion='entropy', max_features='auto', random_state=1)
RF_classifier6.fit(X_train,Y_train)
Y_pred6=RF_classifier6.predict(X_test)# testing
imp_features = Series(RF_classifier6.feature_importances_, index=list(X)).sort_values(ascending=False)
print(imp_features)

# # Using pipeline (method #3) using the most important features
X3 = data2[['MonthlyIncome', 'Age','NumCompaniesWorked','OverTime','EnvironmentSatisfaction']]
X_scaled = StandardScaler().fit_transform(X3)

RF_classifier7 = Pipeline([('balancing', SMOTE(random_state = 101)),
('classification', ensemble.RandomForestClassifier(criterion='entropy', max_features='auto', random_state=1) )])
no_trees = {'classification__n_estimators': [200,250,300,350,400]}
grid_search4 = GridSearchCV(estimator=RF_classifier7, param_grid=no_trees, scoring='recall', cv=5)
grid_search4.fit(X_scaled, Y)

best_parameters = grid_search4.best_params_
print(best_parameters)
best_result = grid_search4.best_score_
print(best_result)