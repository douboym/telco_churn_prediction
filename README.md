# 📞 Telco Customer Churn Prediction

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge.svg)](https://telcochurnprediction-8uly83uimrtk2ypx7xxmuy.streamlit.app/)

## 📌 Présentation du projet

Ce projet vise à prédire si un client d'une entreprise de télécommunications est susceptible de **résilier son contrat (churn)** à l’aide d’algorithmes de Machine Learning.  
L’objectif est d’**aider les équipes commerciales à identifier les clients à risque** pour agir en amont et améliorer la fidélisation.

---

## 🔗 Démo en ligne

🎯 [**Accéder à l'application Streamlit**](https://telcochurnprediction-8uly83uimrtk2ypx7xxmuy.streamlit.app/)

---

## 📂 Source des données

Les données utilisées proviennent du dataset public disponible sur Kaggle :  
🔗 [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🛠️ Technologies utilisées

- Python 3.11  
- Pandas, NumPy  
- Scikit-learn (Logistic Regression, preprocessing, évaluation)  
- XGBoost, LightGBM, Gradient Boosting, SVM  
- Matplotlib, Seaborn (visualisation)  
- Streamlit (développement d’une application web interactive)  
- Joblib (sérialisation du modèle)

---

## 📊 Workflow du projet

### 1. 🔍 Exploration et nettoyage des données
- Analyse des variables numériques et catégorielles  
- Suppression des valeurs manquantes  
- Encodage des variables  
- Feature engineering sur `tenure`

### 2. 🤖 Modélisation
- Régression Logistique (avec et sans équilibrage des classes)  
- XGBoost  
- Gradient Boosting  
- SVM (SVC)  
- LightGBM  
- Gestion du déséquilibre avec `class_weight` et `scale_pos_weight`

### 3. 📈 Évaluation
- Métriques : Accuracy, Precision, Recall, F1-Score, ROC-AUC  
- Matrice de confusion  
- Courbe ROC

### 4. 🌐 Application Web
- Interface Streamlit personnalisée  
- Formulaire interactif pour renseigner un client  
- Prédiction automatique et affichage visuel du risque de churn  
- Thème sombre + design structuré par sections (infos générales, services, paiement)

---

## 🧠 À propos

Projet réalisé par **Mamadou DIEDHIOU**  
📫 Pour toute question ou collaboration, n'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/diedhiou/)

