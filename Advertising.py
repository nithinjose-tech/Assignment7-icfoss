#Loading the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

#Calling the model we saved above:

pickle_in = open('advertisement.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:

st.title('Sales Revenue Prediction')
TV= st.number_input("Cost on TV Ad:")
Radio= st.number_input("Cost on Radio Ad:")
Newspaper=st.number_input("Cost on Newspaper Ad:")
submit = st.button('Predict')
if submit:
    prediction = classifier.predict([[TV, Radio, Newspaper]])
    st.write('Predicted sales revenue is:',prediction[0][0],)
