
# **Bangalore House Price Prediction 🚀**

This project predicts house prices in Bangalore using a machine learning model served through a Flask API. It includes a **Streamlit frontend** to provide an intuitive user interface, allowing users to input property details and get estimated prices.

---

## **Project Structure**

```
HousePricePrediction/
│
├── client/                     # Streamlit frontend for user interaction
│   └── client.py               # Streamlit app code
│
├── model/                      # Machine Learning model-related code
│   ├── model_training.ipynb    # Notebook for model training
│   └── columns.json            # JSON file with location data for predictions
│
├── server/                     # Backend server code using Flask
│   └── server.py               # Flask app to serve the model
│
└── README.md                   # Documentation for the project
```

---

## **Technologies Used**
- **Python**: Programming language
- **Flask**: For backend API to serve predictions
- **Streamlit**: For frontend web interface
- **scikit-learn**: Machine learning model
- **Pandas, NumPy**: Data processing
- **Render**: Backend API deployment

---

## **How to Run the Project Locally**

### **1. Clone the Repository**
```bash
git clone https://github.com/Dhruv110903/HousePricePrediction.git
cd HousePricePrediction
```

### **2. Install Dependencies**
Make sure you have Python installed. Install the required packages using:

```bash
pip install -r requirements.txt
```

### **3. Run the Flask Backend**
1. Navigate to the `server/` folder:
   ```bash
   cd server
   ```

2. Run the Flask server:
   ```bash
   python server.py
   ```

The backend server will start on `http://127.0.0.1:5000`.

### **4. Run the Streamlit Frontend**
1. Open a new terminal window and navigate to the `client/` folder:
   ```bash
   cd client
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run client.py
   ```

3. Open the app in your browser at `http://localhost:8501`.

---

## **How to Use the Application**

1. **Enter Square Feet Area**: Input the area in square feet.
2. **Enter BHK**: Specify the number of bedrooms, halls, and kitchens.
3. **Enter Bathrooms**: Provide the number of bathrooms.
4. **Select Location**: Choose from a list of locations in Bangalore.
5. **Click 'Predict Prices'**: View the estimated price in lakhs.

---

## **Backend Deployment**

The backend API is deployed using Render. The endpoint is:
```
https://housepriceprediction-jj33.onrender.com/predict_home_prices
```

---

## **Example Input and Output**

**Input:**
- Area: 1500 sq. ft.
- BHK: 3
- Bathrooms: 2
- Location: Whitefield

**Output:**
- **Estimated Price**: ₹85 Lakhs

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**
For any inquiries or suggestions, feel free to contact me via [GitHub](https://github.com/Dhruv110903).
