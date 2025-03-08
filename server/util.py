import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Get the absolute path of the directory where util.py is located
    script_dir = os.path.dirname(__file__)
    artifacts_dir = os.path.join(script_dir, 'artifacts')

    with open(os.path.join(artifacts_dir, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    with open(os.path.join(artifacts_dir, "banglore_home_pricesp_model.pickle"), "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

# Make sure to load artifacts when the module is imported
load_saved_artifacts()
