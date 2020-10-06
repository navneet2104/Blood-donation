import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.write("""
# Blood Donation for Future Prediction app
This app predicts whether a person will donate blood in 2007 or not
""")

st.sidebar.header('User Input parameter')

def user_input_features():
     Recency  = st.sidebar.slider('Recency', 0, 74)
     Frequency= st.sidebar.slider('Frequency', 1,43)
     Monetary = st.sidebar.slider('Monetary', 250,12500)
     Time = st.sidebar.slider('Time', 2,98)
     
     data = {'Recency (months)': Recency  ,
           'Frequency (times)': Frequency,
           'Monetary (c.c. blood)': Monetary,
           'Time (months)':Time}
           
           
     features = pd.DataFrame(data, index=[0])
     return features

df = user_input_features()

st.write(df)

trans = pd.read_csv('transfusion.csv')

X_train,X_test,y_train,y_test = train_test_split(trans.drop(columns=['target']), trans['target'].values,test_size=0.2, random_state=24)

clf = LogisticRegression()
clf.fit(X_train, y_train)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)



st.subheader('Prediction')
st.write(trans.target[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
