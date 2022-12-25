import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

pickle_in = open('model.pkl', 'rb') 
model = pickle.load(pickle_in)




def get_prediction(data,model):
    """
    Predict the class of a given data point.
    """
    return model.predict(data)
