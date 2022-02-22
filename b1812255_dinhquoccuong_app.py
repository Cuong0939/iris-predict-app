import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Welcome to IRIS predictions')
st.markdown("<h1 style='text-align: left; width:100rem;margin-left:-30rem;'>Please enter your flower measurements below:</h1>", unsafe_allow_html=True)

sepal_length = st.text_input("Please enter sepal length:",)
sepal_width = st.text_input("Please enter sepal width:")
petal_length = st.text_input("Please enter pepal length:")
petal_width = st.text_input("Please enter pepal width:")



def predict(sepal_length,sepal_width,petal_length,petal_width):
    if sepal_length=="" or sepal_width=="" or petal_length=="" or petal_width=="" :
        pass
    else:
        model = joblib.load("iris_model.pkl")
        try:
            value_predict = np.array([float(sepal_length),float(sepal_width),float(petal_length),float(petal_width)]).reshape(1,-1)
            result = model.predict(value_predict)
            return result
        except:
            st.write("input must be digit")
        
        

if st.button('display'):
    result = predict(sepal_length,sepal_width,petal_length,petal_width)
    if result =="Setosa":
        st.image("setosa.png",width=300)
    elif result =="Versicolor":
        st.image("versicolor.png",width=300)
    elif result == "Virginica":
        st.image("virginica.png",width=300)
    else:
        st.write("No result")

  
