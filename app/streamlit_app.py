import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_churn

st.set_page_config(page_title="Telco Customer Churn Prediction", page_icon="📈", layout="wide")

st.title("📞 Telco Customer Churn Prediction")
st.write("Bienvenue sur l'application de prédiction du churn client. Remplissez les informations ci-dessous.")

# --- SECTION Informations générales ---
with st.container():
    st.subheader("📋 Informations Générales")
    col1, col2 = st.columns(2)
    with col1:
        SeniorCitizen = st.selectbox("Senior Citizen ?", [0, 1])
        tenure = st.slider("Tenure (en mois)", 0, 72, 1)
        MonthlyCharges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
        TotalCharges = st.number_input("Total Charges ($)", 0.0, 10000.0, 400.0)
    with col2:
        gender_Male = st.selectbox("Gender: Male ?", [0, 1])
        Partner_Yes = st.selectbox("Partner: Yes ?", [0, 1])
        Dependents_Yes = st.selectbox("Dependents: Yes ?", [0, 1])
        PaperlessBilling_Yes = st.selectbox("Paperless Billing: Yes ?", [0, 1])

# --- SECTION Services ---

with st.expander("🔌 Services d'abonnement"):
    col1, col2 = st.columns(2)
    with col1:
        PhoneService_Yes = st.selectbox("Phone Service: Yes ?", [0, 1])
        MultipleLines_No_phone_service = st.selectbox("Multiple Lines: No Phone Service ?", [0, 1])
        MultipleLines_Yes = st.selectbox("Multiple Lines: Yes ?", [0, 1])
        InternetService_Fiber_optic = st.selectbox("Internet Fiber Optic ?", [0, 1])
        InternetService_No = st.selectbox("No Internet Service ?", [0, 1])
        OnlineSecurity_No_internet_service = st.selectbox("Online Security: No Internet Service ?", [0, 1])
        OnlineSecurity_Yes = st.selectbox("Online Security: Yes ?", [0, 1])
    with col2:
        OnlineBackup_No_internet_service = st.selectbox("Online Backup: No Internet Service ?", [0, 1])
        OnlineBackup_Yes = st.selectbox("Online Backup: Yes ?", [0, 1])
        DeviceProtection_No_internet_service = st.selectbox("Device Protection: No Internet Service ?", [0, 1])
        DeviceProtection_Yes = st.selectbox("Device Protection: Yes ?", [0, 1])
        TechSupport_No_internet_service = st.selectbox("Tech Support: No Internet Service ?", [0, 1])
        TechSupport_Yes = st.selectbox("Tech Support: Yes ?", [0, 1])
        StreamingTV_No_internet_service = st.selectbox("Streaming TV: No Internet Service ?", [0, 1])
        StreamingTV_Yes = st.selectbox("Streaming TV: Yes ?", [0, 1])
        StreamingMovies_No_internet_service = st.selectbox("Streaming Movies: No Internet Service ?", [0, 1])
        StreamingMovies_Yes = st.selectbox("Streaming Movies: Yes ?", [0, 1])

# --- SECTION Contrat et Paiement ---

with st.expander("💳 Contrat et Paiement"):
    col1, col2 = st.columns(2)
    with col1:
        Contract_One_year = st.selectbox("Contract: One year ?", [0, 1])
        Contract_Two_year = st.selectbox("Contract: Two year ?", [0, 1])
    with col2:
        PaymentMethod_Credit_card = st.selectbox("Payment: Credit Card (Automatic) ?", [0, 1])
        PaymentMethod_Electronic_check = st.selectbox("Payment: Electronic Check ?", [0, 1])
        PaymentMethod_Mailed_check = st.selectbox("Payment: Mailed Check ?", [0, 1])

# --- BOUTON ---
if st.button("🔮 Prédire le Churn", type="primary"):
    input_client = [
        SeniorCitizen, tenure, MonthlyCharges, TotalCharges, gender_Male, Partner_Yes, Dependents_Yes,
        PhoneService_Yes, MultipleLines_No_phone_service, MultipleLines_Yes,
        InternetService_Fiber_optic, InternetService_No, OnlineSecurity_No_internet_service,
        OnlineSecurity_Yes, OnlineBackup_No_internet_service, OnlineBackup_Yes,
        DeviceProtection_No_internet_service, DeviceProtection_Yes, TechSupport_No_internet_service,
        TechSupport_Yes, StreamingTV_No_internet_service, StreamingTV_Yes, StreamingMovies_No_internet_service,
        StreamingMovies_Yes, Contract_One_year, Contract_Two_year,
        PaperlessBilling_Yes, PaymentMethod_Credit_card, PaymentMethod_Electronic_check, PaymentMethod_Mailed_check
    ]
    prediction = predict_churn(input_client)

    if prediction == 1:
        st.error("⚠️ Le client est susceptible de **churner** !")
    else:
        st.success("✅ Le client est probablement **fidèle**.")

