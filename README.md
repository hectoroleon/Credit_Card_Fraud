# Credit Card Fraud

# Fraud Detection using Machine Learning

This project detects fraudulent credit card transactions using a Random Forest model. It includes  data exploration, model training, and a Flask API containerized with Docker.

## Dataset Description
The dataset from Kaggle includes features like:
- `distance_from_home`: Distance from home where the transaction occurred.
- `distance_from_last_transaction`: Distance from the last transaction.
- `ratio_to_median_purchase_price`: Ratio of transaction amount to median purchase price.
- `repeat_retailer`, `used_chip`, `used_pin_number`, `online_order`: Transaction details.
- `fraud`: Target variable (1 for fraudulent, 0 for legitimate).

## Project Structure

CREDIT_CARD_FRAUD

├── data/credit_card_data.csv # Dataset

├── docker_image/saved-image.tar # Saved Docker image

├── model/rf_fraud_detection.pkl # Trained Random Forest model

├── app.py # Flask API

├── Dockerfile # Dockerfile

├── EDA_Model.ipynb # EDA and model training

├── LICENSE # License file

├── README.md # Project documentation

└── requirements.txt # Python dependencies

### Model and Docker Image Storage

Due to size constraints, the trained model and Docker image are stored in Google Drive. You can access them using the following link:

https://drive.google.com/drive/folders/1_7sUohckLqtr52vtBXwEhVoPxJz1mMYt?usp=drive_link


## Steps in the Project
1. **Data Collection**: Dataset sourced from Kaggle.
2. **EDA**: Explored data distributions, correlations, and class imbalance.
3. **Model Training**: Trained Logistic Regression, Random Forest, and XGBoost models.
4. **Model Selection**: Random Forest performed best:
   - **Accuracy**: 99%
   - **ROC-AUC**: 0.992
   - **False Positives**: 1,333
   - **False Negatives**: 17
5. **Flask API**: Developed an API to serve predictions.
6. **Dockerization**: Containerized the API and saved the image (`saved-image.tar`).

## How to Use
1. **Load Docker Image**:
   
   ```bash
   docker load -i docker_image/saved-image.tar
   
2. **Run Container**
   ```bash
   docker run -p 5000:5000 fraud-detection-api
   
3. **Test API**
   ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
    "ratio_to_median_purchase_price": 1.5,
    "online_order": 1,
    "distance_from_home": 25.0,
    "distance_from_last_transaction": 10.0,
    "used_pin_number": 0
    }' http://127.0.0.1:5000/predict

## Future Deployment
1. **Push the Docker image to Docker Hub:**
   ```bash
    docker tag fraud-detection-api <your-dockerhub-username>/fraud-detection-api:latest
    docker push <your-dockerhub-username>/fraud-detection-api:latest
3. **Deploy to a cloud platform**
