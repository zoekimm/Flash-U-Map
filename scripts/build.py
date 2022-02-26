import numpy as np
import pandas as pd
from itertools import chain
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
from sklearn.ensemble import RandomForestClassifier
#from sklearn.tree import DecisionTreeClassifier


def train():
    final_df = pd.read_csv('compiled_data2.csv')
    final_df = final_df.drop('Unnamed: 0', axis = 1)
    X = final_df.iloc[:, :-1]
    y = final_df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=42)

    #clf_model = DecisionTreeClassifier(criterion="gini", random_state = 42, max_depth = 2, min_samples_leaf = 5)   
    #clf_model.fit(X_train, y_train)
    #y_predict = clf_model.predict(X_test)
    #accuracy_score(y_test, y_predict)

    rf = RandomForestClassifier(max_depth = 2, max_features = 3, n_estimators = 15, random_state = 2)
    rf.fit(X_train, y_train)

    return rf 


