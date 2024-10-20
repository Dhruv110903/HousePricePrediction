from flask import Flask, request, jsonify
import json
import pickle
import numpy as np
import warnings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICKLE_PATH = os.path.join(BASE_DIR, "artifacts", "home_prediction_model.pickle")


# Global variables
__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("Loading saved artifacts... start!")
    global __data_columns
    global __locations

    # Load data columns
    __data_columns = columns_data['data_columns']
    __locations = __data_columns[3:]

    # Load the model
    global __model
    os.makedirs(os.path.dirname(PICKLE_PATH), exist_ok=True)
    with open(PICKLE_PATH, 'rb') as f:
    # with open("server/artifacts/home_prediction_model.pickle", 'rb') as f:
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

