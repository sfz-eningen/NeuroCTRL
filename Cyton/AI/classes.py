from brainflow import *
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib



class Train():

    def __init__(self): 
        f = open("./samples/samples.csv", "r")
        s = f.read().replace(",", ".")
        f.close()
        f = open("./samples/samples.csv", "w")
        f.write(s)
        f.close()
        data = pd.read_csv("./samples/samples.csv", sep=";")
        print(data.head())
        y = data.ACTION
        
        X = data.drop('ACTION', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                            test_size=0.2, 
                                                            random_state=123, 
                                                            stratify=y)
        print(list(y_test))
        scaler = preprocessing.StandardScaler().fit(X_train)
        X_train_scaled = scaler.transform(X_train)
        pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))
        #print(pipeline.get_params())
        hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                            'randomforestregressor__max_depth': [None, 5, 3, 1]}
        clf = GridSearchCV(pipeline, hyperparameters, cv=10)
        
        # Fit and tune model
        clf.fit(X_train, y_train)
        print(X_test)
        y_pred = clf.predict(X_test)
        print(y_pred, list(y_test))
        print(r2_score(y_test, y_pred))