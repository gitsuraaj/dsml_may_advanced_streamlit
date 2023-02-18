import streamlit as st
import datetime
import pickle
import pandas as pd


st.write (""" # Cars 24 Used Car Prediction App!""")


col1, col2=st.columns (2)

fuel_type_1 = st.selectbox("Select Fuel Type",
                        ["Diesel", "Petrol" , "CNG", "LPG", "electric"])
transmission_type = st.selectbox("Select Transmission Type",["Manual", "Automatic"])
engine = st.slider('Select Engine Power',500, 5000, step=100)
seats = st.selectbox("Select no. of seats",[4,5,6,7,8])

encode_dict={
    "fuel_type": {"Diesel":1, "Petrol":2 , "CNG": 3, "LPG":4 , "electric":5},
    "transmission_type": {"Manual":1 , "Automatic": 2}
}


def model_pred (fuel_type, transmission_type, engine, seats):
    with open ("car_pred", "rb") as file:
        reg_model= pickle.load(file)

    input_ftrs=[[2018.0,1,40000, fuel_type, transmission_type, 19.70, engine,886.30, seats]]

    return reg_model.predict (input_ftrs)



if st.button('Predict Car Price'):
    fuel_type= encode_dict['fuel_type'][fuel_type_1]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price=model_pred (fuel_type, transmission_type, engine, seats)
    st.text ("Predicted Price of the car is "+ str(price))