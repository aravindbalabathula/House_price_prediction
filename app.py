import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model using pickle
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict house price
def predict_house_price(area, bedrooms, stories, mainroad, parking, prefarea, furnishingstatus):
    # Creating a DataFrame for the input features
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'stories': [stories],
        'mainroad': [mainroad],
        'parking': [parking],
        'prefarea': [prefarea],
        'furnishingstatus': [furnishingstatus]
    })
    
    # Make prediction
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Streamlit UI
st.title('House Price Prediction')

st.header('Enter the details of the house:')

# Input fields for the features
area = st.number_input('Area (in sqft):', min_value=1)
bedrooms = st.number_input('Number of Bedrooms:', min_value=1)
stories = st.number_input('Number of Stories:', min_value=1)
mainroad = st.selectbox('Main Road (Yes/No):', ['No', 'Yes'])
parking = st.number_input('Number of Parking Spaces:', min_value=0)
prefarea = st.selectbox('Preferred Area (Yes/No):', ['No', 'Yes'])
furnishingstatus = st.selectbox('Furnishing Status:', ['Unfurnished', 'Semi-furnished', 'Fully-furnished'])

# Convert categorical inputs to numerical values
mainroad = 1 if mainroad == 'Yes' else 0
prefarea = 1 if prefarea == 'Yes' else 0
furnishingstatus = {'Unfurnished': 0, 'Semi-furnished': 1, 'Fully-furnished': 2}[furnishingstatus]

# Button to trigger prediction
if st.button('Predict Price'):
    # Call the prediction function
    predicted_price = predict_house_price(area, bedrooms, stories, mainroad, parking, prefarea, furnishingstatus)
    
    # Display the predicted price
    st.subheader(f'Predicted House Price: ₹{predicted_price*1e5:,.2f}')
