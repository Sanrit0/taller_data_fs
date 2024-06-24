from flask import Flask, jsonify, request, abort
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)

ruta_actual = os.path.abspath(__file__)
os.chdir(os.path.dirname(ruta_actual))

model = pd.read_pickle('models/model.pkl')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the housing API!'})

@app.route('/predict', methods=['POST'])
def predict():

    if 'surface' in request.args:
        surface = int(request.args.get('surface'))
    else:
        abort(404, 'You must provide a surface.')

    if 'bedrooms' in request.args:
        bedrooms = int(request.args.get('bedrooms'))
    else:
        abort(404, 'You must provide number of bedrooms.')

    if 'restrooms' in request.args:
        restrooms = int(request.args.get('restrooms'))
    else:
        abort(404, 'You must provide number of restrooms.')

    input_data = [[surface, bedrooms, restrooms]]
    prediction = model.predict(input_data)

    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")