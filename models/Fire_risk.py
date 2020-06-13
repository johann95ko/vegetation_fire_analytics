import os
import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LinearRegression

cwd = os.getcwd()

class Risk_regression_model():
    """ This model designates a fire risk score """

    def train(self, training_set_url):
        df = pd.read_csv(training_set_url)
        df.dropna(how='all')

        x_train = df.iloc[:,0:5]
        y_train = df.iloc[:,5]
        
        reg = LinearRegression().fit(x_train, y_train)


        with open(os.path.join(cwd, 'output', 'linear_model.pkl'), 'wb') as handle:
            pickle.dump(reg, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return 'success'


    def predict(self, 
                temp:float, 
                is_raining:int, 
                is_sunny:int, 
                humidity:float, 
                have_combustible:int
        ):
        with open(os.path.join(cwd, 'output', 'linear_model.pkl'), 'rb') as handle:
            reg = pickle.load(handle)
        
        pred_x = np.array([[temp, is_raining, is_sunny, humidity, have_combustible]])
        pred_y = reg.predict(pred_x)

        return min(1, max(0, pred_y.item(0)))