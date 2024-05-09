# -*- coding: utf-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json

app = FastAPI()

class model_input(BaseModel):
    Gravel: int
    Soil: int
    Bed_rock: int
    Distance_from_river_swat: float
    Diameter_of_Well: float
          
        
# loading the saved model
model = joblib.load(open('model.joblib', 'rb'))

@app.post('/groundwater_prediction')
def groundwaterlevel_pred(input_parameters: model_input):
    # Confirm API call at the start of the function
    print("API call received. Processing request...")

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    gravel = input_dictionary['Gravel']
    soil = input_dictionary['Soil']
    bed_rock = input_dictionary['Bed_rock']
    Distance_from_river_swat = input_dictionary['Distance_from_river_swat']
    Diameter_of_Well = input_dictionary['Diameter_of_Well']
    
    input_list = [gravel, soil, bed_rock, Distance_from_river_swat, Diameter_of_Well]
    
    prediction = model.predict([input_list])

    # Convert prediction result to a list before returning
    prediction_list = prediction.tolist()

    return prediction_list
    
    return prediction
