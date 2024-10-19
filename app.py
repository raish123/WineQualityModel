from flask import Flask,render_template,redirect,url_for,request
import os,sys,pandas as pd,numpy as np
from src.Wine.Exception import CustomException
from src.Wine.loggers import logger
from src.Wine.Pipelines.prediction import PredictionPipeline



#creating an object of  Flask class
app = Flask(__name__)



#creating route to show index page 
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



#here we are creating 2 routes 1 for training the model and 2nd for prediction the model
@app.route('/train',methods=['GET','POST'])
def train():
    os.system("main.py") #system is a built in method of os module we used them for executable command
    return "Training Done Successfully"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed acidity'])
            volatile_acidity =float(request.form['volatile acidity'])
            citric_acid =float(request.form['citric acid'])
            residual_sugar =float(request.form['residual sugar'])
            #chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free sulfur dioxide'])
            total_sulfur_dioxide =float(request.form['total sulfur dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
            #quality =float(request.form['quality'])
            Id =float(request.form['Id'])
       
         
            # Creating a dictionary of the new datapoint
            data = {
                'fixed_acidity': [fixed_acidity],
                'volatile_acidity': [volatile_acidity],
                'citric_acid': [citric_acid],
                'residual_sugar': [residual_sugar],
                'free_sulfur_dioxide': [free_sulfur_dioxide],
                'total_sulfur_dioxide': [total_sulfur_dioxide],
                'density': [density],
                'pH': [pH],
                'sulphates': [sulphates],
                'alcohol': [alcohol],
                'Id': [Id]
            }

            df = pd.DataFrame(data)
            
            obj = PredictionPipeline()
            predict = obj.predict(data_dict=df)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')








if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)