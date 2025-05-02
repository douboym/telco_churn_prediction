import joblib
import numpy as np
import os

# Charger modèle et scaler avec chemins relatifs
model = joblib.load(os.path.join('models', 'logreg_balanced.pkl'))
scaler = joblib.load(os.path.join('models', 'scaler.pkl'))

# Fonction de prédiction
def predict_churn(input_data):
    input_scaled = scaler.transform(np.array(input_data).reshape(1, -1))
    prediction = model.predict(input_scaled)
    return prediction[0]


