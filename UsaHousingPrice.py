# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:13:44 2021

@author: 91892
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import pickle
lr_pipe = pickle.load(open('lr_pipe', 'rb'))

st.title('USA Housing Price Prediction')
st.subheader('by Anshu')
st.markdown('----')
st.balloons()

Avg_Area_Income = int(st.number_input('Enter the Average Area Income: '))

Avg_Age_of_House = int(st.number_input('Enter the Avg. Age of House : '))

Avg_Number_of_Rooms_in_Area = int(st.number_input('Enter the Avg_Number_of_Rooms_in_Area: '))

Avg_Number_of_Bedrooms_in_Area = int(st.number_input('Enter the Avg_Number_of_Bedrooms_in_Area: '))

Area_Population = int(st.number_input('Enter the Area_Population: '))

inputs=np.array([[Avg_Area_Income, Avg_Age_of_House, Avg_Number_of_Rooms_in_Area, Avg_Number_of_Bedrooms_in_Area, Area_Population]])

def predict_Strokes(Avg_Area_Income, Avg_Age_of_House, Avg_Number_of_Rooms_in_Area, Avg_Number_of_Bedrooms_in_Area, Area_Population):
                prediction=lr_pipe.predict(inputs)
                return prediction
            
            
if st.button("Prediction"):
    prediction = predict_Strokes(Avg_Area_Income, Avg_Age_of_House, Avg_Number_of_Rooms_in_Area, Avg_Number_of_Bedrooms_in_Area, Area_Population)
    st.success(f'House Price will be: ${round(int(prediction),2)}')