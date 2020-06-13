import json
import os
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
authenticator = IAMAuthenticator(os.getenv("WATSON_VISUAL_RECOG_API_KEY"))

COMBUSTIBLE_OBJ={'plant', 'grass', 'wood', 'paper', 'cardboard', 'cigarette', 'leaf', 'leaves'}

def visual_recog(frame:str):
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

    if (pred_classes & COMBUSTIBLE_OBJ): 
        return 1
    else: 
        return 0