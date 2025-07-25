Customer Churn Prediction Project
=================================

Overview
--------
This project predicts whether a telecom customer is likely to churn (leave the service) 
based on their account details and service usage. The model uses machine learning 
to analyze customer behavior and generate churn predictions.

Dataset
-------
The dataset used is the "Telco Customer Churn Dataset" (WA_Fn-UseC_-Telco-Customer-Churn.csv).
It contains customer demographics, account information, and service usage details.

Project Steps
-------------
1. Exploratory Data Analysis (EDA) to identify patterns and trends.
2. Data preprocessing (encoding categorical variables, scaling numeric values).
3. Model training using Logistic Regression, RandomForest, and XGBoost.
4. Hyperparameter tuning with GridSearchCV and RandomizedSearchCV.
5. Evaluation based on Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
6. Saving the best model as "churn_model.pkl" for deployment.
7. Developing an interactive Streamlit dashboard for predictions.

Technologies Used
-----------------
- Python (Pandas, NumPy, Scikit-learn, XGBoost, Seaborn, Matplotlib)
- Streamlit (for the dashboard)
- Joblib (for saving models)

How to Run
----------
1. Clone the project and place the dataset and saved model in the project folder.
2. Install the required dependencies:

   pip install streamlit pandas scikit-learn xgboost joblib

3. Run the Streamlit app:

   streamlit run app.py

4. Open the local URL displayed in the terminal to use the app.

Streamlit App Features
----------------------
- Interactive form for entering customer details.
- Predicts churn probability and decision (Churn / Not Churn).
- User-friendly interface with clear results.

Goal
----
The goal of this project is to help telecom companies identify high-risk customers 
so they can take proactive steps to retain them and reduce churn rates.
