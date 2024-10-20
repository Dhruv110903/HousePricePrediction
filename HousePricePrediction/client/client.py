import streamlit as st
import json
import requests

st.title("Bangalore House Price Prediction")

# Input Fields
st.header("Area")
area = st.text_input("Enter square ft. area")

st.header("BHK")
bhk = st.text_input("Enter how many BHK?")

st.header("Bathroom")
bathroom = st.text_input("Enter the number of bathrooms")

st.header("Location")
with open('/Users/dhruv/Desktop/ML/HousePricePrediction/model/columns.json', 'r') as f:
    data = json.load(f)

locations = data['data_columns'][3:]

location = st.selectbox("Choose any 1 location", locations,index=None)

# Button for Prediction
if st.button("Predict Prices"):
    try:
        # Convert inputs to appropriate types
        input_data = {
            "total_sqft": float(area) if area else 0.0,
            "location": location,
            "bath": int(bathroom) if bathroom else 0,
            "bhk": int(bhk) if bhk else 0
        }
        # if we want localhost
        # url = "http://127.0.0.1:5000/predict_home_prices"  
        
        # deployed backend server
        url="https://housepriceprediction-jj33.onrender.com/predict_home_prices"

        # Send POST request
        response = requests.post(url, data=input_data)

        # Debugging information
        print(f"Request Data: {input_data}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # Handle response
        if response.status_code == 200:
            result = response.json()
            estimated_price = int(float(result.get('Estimated Price')))
            st.header(f'Estimated Price in Lakhs: {estimated_price}')
        else:
            st.error(f"Request failed with status: {response.status_code}")
            st.error(f"Response: {response.text}")

    except ValueError:
        st.error("Invalid input. Please enter correct values.")
