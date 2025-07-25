<!DOCTYPE html>
<html>
<head>
    <title>Customer Churn Prediction Project</title>
</head>
<body>

    <h1>Customer Churn Prediction</h1>

    <h2>Overview</h2>
    <p>
        This project predicts whether a telecom customer is likely to churn (leave the service) 
        based on their account information and service usage. The model uses machine learning 
        techniques to analyze customer behavior and generate churn predictions.
    </p>

    <h2>Dataset</h2>
    <p>
        The dataset used is the <b>Telco Customer Churn Dataset</b> 
        (WA_Fn-UseC_-Telco-Customer-Churn.csv). 
        It contains customer demographics, account information, and service usage details.
    </p>

    <h2>Project Steps</h2>
    <ol>
        <li>Exploratory Data Analysis (EDA) to find patterns and insights.</li>
        <li>Data preprocessing (encoding categorical variables, scaling numeric ones).</li>
        <li>Model training with Logistic Regression, RandomForest, and XGBoost.</li>
        <li>Hyperparameter tuning using GridSearchCV and RandomizedSearchCV.</li>
        <li>Model evaluation based on Accuracy, Precision, Recall, F1 Score, and ROC-AUC.</li>
        <li>Saving the best model as <b>churn_model.pkl</b> for deployment.</li>
        <li>Building a Streamlit app for interactive churn prediction.</li>
    </ol>

    <h2>Technologies Used</h2>
    <ul>
        <li>Python (Pandas, NumPy, Scikit-learn, XGBoost, Seaborn, Matplotlib)</li>
        <li>Streamlit for interactive dashboard</li>
        <li>Joblib for model persistence</li>
    </ul>

    <h2>How to Run</h2>
    <ol>
        <li>Clone the project and place the dataset and saved model in the project folder.</li>
        <li>Install required packages:
            <pre><code>pip install streamlit pandas scikit-learn xgboost joblib</code></pre>
        </li>
        <li>Run the app:
            <pre><code>streamlit run app.py</code></pre>
        </li>
        <li>Open the local URL displayed in the terminal to access the app.</li>
    </ol>

    <h2>Streamlit App Features</h2>
    <ul>
        <li>Interactive form for entering customer details.</li>
        <li>Predicts churn probability and decision (Yes/No).</li>
        <li>Displays results in a clear, user-friendly interface.</li>
    </ul>

    <h2>Goal</h2>
    <p>
        The goal of this project is to help telecom companies identify high-risk customers 
        so they can take proactive measures to retain them and reduce churn rates.
    </p>

</body>
</html>
