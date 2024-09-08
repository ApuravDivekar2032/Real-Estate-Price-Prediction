from flask import Flask, request, jsonify, send_from_directory
import os
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Real Estate Price Prediction API"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/client/<path:app.html>')
def serve_client_static():
    return send_from_directory('client', app.html)

@app.route('/client/<path:app.css>')
def serve_client_static():
    return send_from_directory('client', app.css)

@app.route('/client/<path:app.js>')
def serve_client_static():
    return send_from_directory('client', app.js)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
