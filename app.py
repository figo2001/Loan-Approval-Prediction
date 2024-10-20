from flask import request, render_template, Flask
import pickle

import numpy as np
import pandas as pd

# Creates a Flask app instance.
app=Flask(__name__)

# Loading the Models
model=pickle.load(open('CatBoost.pkl', 'rb'))

scaler=pickle.load(open('Scaler.pkl', 'rb'))


# Prediction Function
def predict(model,scaler,person_age, person_income, person_home_ownership,person_emp_length, loan_intent, loan_grade, 
                       loan_amnt,loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length):
    
    features=np.array([[person_age, person_income, person_home_ownership,person_emp_length, loan_intent, loan_grade, 
                       loan_amnt,loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]])
    
    scaled_features=scaler.transform(features)
    
    result=model.predict(scaled_features)
    
    return result[0]




# Defines the route for the home page.
@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method=='POST':
        person_age=(request.form['person_age'])
        person_income=(request.form['person_income'])
        person_home_ownership=(request.form['person_home_ownership'])
        person_emp_length=float(request.form['person_emp_length'])
        loan_intent=(request.form['loan_intent'])
        loan_grade=(request.form['loan_grade'])
        loan_amnt=(request.form['loan_amnt'])
        loan_int_rate=float(request.form['loan_int_rate'])
        loan_percent_income=float(request.form['loan_percent_income'])
        cb_person_default_on_file=(request.form['cb_person_default_on_file'])
        cb_person_cred_hist_length=(request.form['cb_person_cred_hist_length'])

        prediction=predict(model,scaler,person_age, person_income, person_home_ownership,person_emp_length, loan_intent, loan_grade, loan_amnt,loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length)
        prediction_text="Loan Approved" if prediction==1 else "Loan not Approved"

        return render_template('index.html', prediction=prediction_text)






if __name__=='__main__':
    app.run(debug=True)