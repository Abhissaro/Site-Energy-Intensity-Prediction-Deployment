
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from prediction import get_prediction


st.set_page_config(page_title='Site Energy Intensity Prediction', page_icon="⚡🌇💫",
                               layout="wide", initial_sidebar_state='expanded')

pickle_in = open('model.pkl', 'rb') 
model = pickle.load(pickle_in)


# creating option list for dropdown menu

features = ['february_avg_temp', 'march_avg_temp', 'december_avg_temp', 'avg_temp',
       'month_heating_degree_days']

st.markdown("<h1 style='text-align: center;'>Site Energy Intensity Prediction App ⚡🌇💫 </h1>", unsafe_allow_html=True)

def main():
    with st.form('prediction_form'):

       st.header("Predict the input for following features:")

       august_avg_temp = st.slider('august_avg_temp', 0.00, 80.00, value=10.00, format="%f")
       december_avg_temp = st.slider('december_avg_temp', 0.00, 80.00 , value=10.00, format="%f")
       avg_temp = st.slider('avg_temp', 0.00, 80.00 , value=10.00, format="%f")
       avg_winter_temp = st.slider('avg_winter_temp', 0.000, 80.000 , value=10.00, format="%f")
       std_spring_temp = st.slider( 'std_spring_temp', 0.00, 80.00, value=10.00, format="%f")
       submit = st.form_submit_button("Predict")

    if submit:
        #'february_avg_temp', 'december_avg_temp', 'cooling_degree_days','avg_temp', 'std_spring_temp'
        #'august_avg_temp', 'december_avg_temp', 'avg_temp', 'avg_winter_temp','std_spring_temp'
       data = np.array(['august_avg_temp', 'december_avg_temp', 'avg_temp','avg_winter_temp', 'std_spring_temp']).reshape(1, -1)
       pred = get_prediction(data=data, model=model)
       st.write(f"The predicted Site Energy Intensity is:  {pred}")


if __name__ == '__main__':
       main()




 

