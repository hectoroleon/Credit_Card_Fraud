from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load saved model
model = joblib.load("model/rf_fraud_detection.pkl")

# Initialize Flask
app = Flask(__name__)

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data
    data = request.get_json()
    
    # Convert input data into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Make a prediction
    prediction = model.predict(input_data)

    # Log the prediction
    print("Prediction:", prediction[0])
    
    # Return the prediction
    return jsonify({
        'prediction': int(prediction[0])  # 0 = Legitimate, 1 = Fraud
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')