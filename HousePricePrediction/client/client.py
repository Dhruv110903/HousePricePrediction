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


# with open('/Users/dhruv/Desktop/ML/HousePricePrediction/model/columns.json', 'r') as f:

# data = json.load(locations)
# print(data)

columns_data={"data_columns": ["total_sqft", "bath", "bhk", "1st block jayanagar", 
"1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi",
"5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", 
"7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", 
"aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", 
"amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", 
"arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya",
 "badavala nagar", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii",
"banashankari stage v", "banashankari stage vi", "banaswadi", "banjara layout",
"bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", 
"battarahalli", "begur", "begur road", "bellandur", "benson town", 
"bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli",
"bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli",
"brookefield", "budigere", "cv raman nagar", "chamrajpet", "chandapura", 
"channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", 
"choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura",
"dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", 
"doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", 
"electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", 
"gm palaya", "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", 
"green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", 
"hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", 
"hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", 
"hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", 
"iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", 
"jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", 
"kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", 
"kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli",
"kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", 
"kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", "konanakunte", 
"koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", 
"lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", 
"mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", 
"mico layout", "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", 
"nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar",
"nehru nagar", "ombr layout", "old airport road", "old madras road", "padmanabhanagar", 
"pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout",
"prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", 
"rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", 
"sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout",
"seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya", "sompura", "sonnenahalli", 
"subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", 
"thubarahalli", "thyagaraja nagar", "tindlu", "tumkur road", "ulsoor", "uttarahalli", 
"varthur", "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", 
"whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]}


locations = columns_data['data_columns'][3:]

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



