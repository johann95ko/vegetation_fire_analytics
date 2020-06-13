# Fire risk analytics model
This is A.I vegetation fire analytics model that utilises IBM Watson vision recognition, Sklearn linear regression model and IBM Db2. The purpose of such a model is to assign a risk score for vegetation fire from a set of images and sensor data. 

## How to run
1. Install and create [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
2. Run `pip install -r requirements.txt`
3. Set .env file

    | Env Variables | Meaning                            |
    | ------------- |:----------------------------------:|
    | FRAME         | An image or a frame from the video |
    | MODE          | Either set to `train` or `predict` |
4. Run `python model.py`