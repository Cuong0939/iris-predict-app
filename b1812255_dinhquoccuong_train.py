# -*- coding: utf-8 -*-
"""B1812255_DinhQuocCuong_train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/128wAR8dUuFzuZnjvanrZybO5JXJYC-EO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib




def load_model(filename=""):
    df = pd.read_csv(filename)
    print("describe of dataset")
    print(df.describe())
    print()
    print("info of datasets")
    print(df.info())
    print('split datasets')
    y = df.pop('variety')
    X = df
    print("Dataset splited")
    print(X.head())
    print(y)
    return X,y

def split_and_make_model(feature,label):
    X_train,X_test,y_train,y_test = train_test_split(feature,label,test_size=0.2,random_state=42)
    model = SVC(kernel="poly")
    model.fit(X_train,y_train)
    predict = model.predict(X_test)
    ac = accuracy_score(y_test,predict)
    print(f"accuracy_score:{ac}")
    print("save model")
    joblib.dump(model, "iris_model.pkl")
    print(f"model saved")
    return model

def __main__():
    filename = "iris.csv"
    feature,label=load_model(filename)
    model = split_and_make_model(feature,label)
    value = [5.1,3.5,1.4,0.2]
    result = predict(model,value)
    print(f"{result}")

def predict(model,value):
    result = model.predict(np.array(value).reshape(1,-1))
    return result
__main__()
