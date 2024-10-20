from flask import Flask,request,jsonify
import warnings

from . import utils  # Use relative import
# this only works, god knows why


app=Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi!"

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response=jsonify({
        'locations':utils.get_location_names()
    })   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_prices',methods=['POST'])
def predict_home_price():
    total_sqft = round(float(request.form['total_sqft']))
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify(
        {
            'Estimated Price': utils.get_estimate_price(location,total_sqft,bath,bhk)
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')

if  __name__ == "__main__": 
    util.load_saved_artifacts()
    app.run()




