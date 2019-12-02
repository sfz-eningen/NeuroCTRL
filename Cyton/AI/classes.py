### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben, Maximilian Menzel
# Last edit:  01.12.2019
# Purpose:    AI Initializer for the "Encephalographic Signal Analysis and Recognition Toolkit",
#             ("ESART")
###
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from brainflow import *
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.externals import joblib
from sklearn.datasets import load_iris

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np
import sys
# Set random seed
def AIIk(text):
    sys.stdout.write(f"\n\x1B[33;1m{text}\x1B[0m\n".replace("<", "\x1B[32m<\x1B[33m").replace(">", "\x1B[32m>\x1B[33m"))
def AII(text):
    sys.stdout.write(f"\n\x1B[35;1m{text}\x1B[0m\n")
def AIN(section, text):
    sys.stdout.write(f"\n\t\x1B[35;1m{section}:{(len('SAMPLE-PREPROCESSING')-len(section)+2)*' '} \x1B[34;1m{text}\x1B[0m\n")
def AINc(section, text):
    sys.stdout.write(f"\n\t\x1B[35;1m{section} {(len('SAMPLE-PREPROCESSING')-len(section)+2)*' '} \x1B[34;1m{text}\x1B[0m\n")
def AINp(section="", text=""):
    sys.stdout.write(f"\t\x1B[35;1m{section}{(len('SAMPLE-PREPROCESSING')-len(section)+2)*' '}  \x1B[34;1m[\x1B[32;1mDONE\x1B[34;1m]\x1B[0m\n")
class brainAI():
    def __init__(self):
        pass
    def train(self, file="./samples/samples.csv"):
        AII(f"Training from '{file}'...")
        AIN("SAMPLE-PREPROCESSING", f"Cleaning up samples in '{file}'...")
        f = open(file, "r")
        s = f.read().replace(",", ".")
        f.close()
        f = open(file, "w")
        f.write(s)
        f.close()
        AINp()
        AIN("LOADING", f"Reading samples from '{file}'...")
        self.data = pd.read_csv(file, sep=";")
        AINp()
        AINc("", f"Creating axes...")
        y = self.data.ACTION
        X = self.data.drop('ACTION', axis=1)
        AINp()
        AIN("PREPROCESSING", f"Splitting data...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                            test_size=0.2, 
                                                            random_state=123, 
                                                            stratify=y)
        AINp()
        AINc("", f"Scaling data...")
        scaler = preprocessing.StandardScaler().fit(X_train)
        X_train_scaled = scaler.transform(X_train)
        AINp()
        AIN("PIPELINE", f"Creating pipeline...")
        pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))
        self.hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                            'randomforestregressor__max_depth': [None, 5, 3, 1]}
        AINp()
        AIN("PREDICTOR", f"Creating predictor...")
        self.clf = GridSearchCV(pipeline, self.hyperparameters, cv=10)
        # Fit and tune model
        self.clf.fit(X_train, y_train)
        AINp()
        AII("AI TRAINED!\nUse {object name}.analyze({data}) to predict.")
    def analyze(self, data):
        # AII("ANALYZING...")
        return self.clf.predict(data)

def dimc(dct):
    data = dct["data"]
    dout = []
    for x in data:
        for y in x:
            dout.append(y)
    return dout