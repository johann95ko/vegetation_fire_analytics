import json
import os
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from models.red_rhino_robot import alert_3r
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
authenticator = IAMAuthenticator(os.getenv("WATSON_VISUAL_RECOG_API_KEY"))

COMBUSTIBLE_OBJ={'plant', 'grass', 'wood', 'paper', 'cardboard', 'cigarette', 'leaf', 'leaves', 'flame', 'fire'}
ALERT_OBJ={'fire', 'flame', 'combustion'}

def visual_recog(frame:str, location_name:str):
    """ IBM Watson visual recognition model"""
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        authenticator=authenticator
    )

    visual_recognition.set_service_url(os.getenv("SERVICE_URL"))

    url = frame
    classes_result = visual_recognition.classify(url=url).get_result()
    
    pred_classes=set()
    for item in classes_result['images'][0]['classifiers'][0]['classes']:
        pred_classes.add(item['class'])
    
    # Check for occurrence of fire and activate red rhino robot accordingly
    if(pred_classes & ALERT_OBJ):
        alert_3r(location_name)

    # Check for combustible
    if (pred_classes & COMBUSTIBLE_OBJ): 
        return 1
    else: 
        return 0