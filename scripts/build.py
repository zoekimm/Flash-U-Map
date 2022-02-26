import numpy as np
import pandas as pd
from itertools import chain
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
from sklearn.ensemble import RandomForestClassifier
#from sklearn.tree import DecisionTreeClassifier

def predict(recorded_data):
    final_df = pd.read_csv('/Users/zoekim/Desktop/g/Safe-U-Map/scripts/compiled_data.csv')
    X = final_df.drop('result', 1).values
    y = final_df['result'].values.astype('int')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=42)

    #clf_model = DecisionTreeClassifier(criterion="gini", random_state = 42, max_depth = 2, min_samples_leaf = 5)   
    #clf_model.fit(X_train, y_train)
    #y_predict = clf_model.predict(X_test)
    #accuracy_score(y_test, y_predict)

    rf = RandomForestClassifier(max_depth=None, max_features=3, n_estimators=15, random_state=2)
    rf.fit(X_train, y_train)

    return rf.predict(recorded_data)

