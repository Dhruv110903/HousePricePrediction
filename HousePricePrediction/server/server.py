from flask import Flask, request, jsonify
import json
import pickle
import numpy as np
import warnings

# Global variables
__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("Loading saved artifacts... start!")
    global __data_columns
    global __locations

    # Load data columns
    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Load the model
    global __model
    with open("server/artifacts/home_prediction_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("Artifacts loaded successfully!")

def get_location_names():
    # Ensure artifacts are loaded before accessing locations
    if __locations is None:
        load_saved_artifacts()
    return __locations

def get_estimate_price(location, sqft, bath, bhk):
    # Ensure artifacts are loaded before processing
    if __data_columns is None or __model is None:
        load_saved_artifacts()

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    # Initialize features array
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1 
    return round(__model.predict([x])[0], 2)

# Flask app setup
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi!"

@app.route('/get_location_names', methods=['GET'])
def get_location_names_route():
    response = jsonify({
        'locations': get_location_names()
    })   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_prices', methods=['POST'])
def predict_home_price():
    total_sqft = round(float(request.form['total_sqft']))
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify(
        {
            'Estimated Price': get_estimate_price(location, total_sqft, bath, bhk)
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')

if __name__ == "__main__": 
    load_saved_artifacts()
    app.run()
