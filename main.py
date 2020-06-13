#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from models.Visual_recog import visual_recog
from models.Fire_risk import Risk_regression_model
from database.db2 import Db2
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

cwd = os.getcwd()

""" Dummy variables from Lamppost-as-a-platform """
location_name='5'
temp= 37.0
is_raining = 0
is_sunny = 1
humidity = 40.0


""" Main code """
def main():
    """ Entry point for Lamppost-as-a-platform """
    risk_regression_model = Risk_regression_model()

    # Trigger model to train or predict
    if os.getenv('MODE') == 'train':
        training_set_url = os.path.join(cwd, 'data', 'fire_risk_train_data.csv')
        risk_regression_model.train(training_set_url=training_set_url)

    elif os.getenv('MODE') == 'predict':
        have_combustible = visual_recog(os.getenv('FRAME'), location_name)
        prediction = risk_regression_model.predict(temp, 
                                      is_raining, 
                                      is_sunny, 
                                      humidity, 
                                      have_combustible)

        # Store in IBM DB2
        db2 = Db2()
        db2.update_table(location_name, prediction)

    return 0

if __name__ == "__main__":
    main()