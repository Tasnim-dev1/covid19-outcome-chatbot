import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load both models
deaths_model = pickle.load(open('deaths_model.pkl', 'rb'))
recovered_model = pickle.load(open('recovered_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Collect inputs from form
    confirmed = float(request.form['Confirmed'])
    active = float(request.form['Active'])
    country = request.form['Country_Region']
    region = request.form['WHO_Region']

    input_data = pd.DataFrame([{
        "Confirmed": confirmed,
        "Active": active,
        "Country_Region": country,
        "WHO_Region": region
    }])

    # Predict using both models
    deaths_pred = round(deaths_model.predict(input_data)[0], 2)
    recovered_pred = round(recovered_model.predict(input_data)[0], 2)

    return render_template('index.html',
                           prediction_text=f'Predicted Deaths: {deaths_pred}, Predicted Recovered: {recovered_pred}')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls
    '''
    data = request.get_json(force=True)

    confirmed = float(data['Confirmed'])
    active = float(data['Active'])
    country = data['Country_Region']
    region = data['WHO_Region']

    input_data = pd.DataFrame([{
        "Confirmed": confirmed,
        "Active": active,
        "Country_Region": country,
        "WHO_Region": region
    }])

    deaths_pred = deaths_model.predict(input_data)[0]
    recovered_pred = recovered_model.predict(input_data)[0]

    return jsonify({
        'Predicted_Deaths': deaths_pred,
        'Predicted_Recovered': recovered_pred
    })

if __name__ == "__main__":
    app.run(debug=True)
