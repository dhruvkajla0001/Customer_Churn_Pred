import streamlit as st
import joblib
import pandas as pd

# ===========================
# Load Model
# ===========================
model = joblib.load("churn_model.pkl")

# ===========================
# Streamlit Page Config
# ===========================
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        .main {background-color: #f8f9fa;}
        .stTabs [role="tablist"] button {font-size:18px; font-weight:bold;}
        .prediction-card {background-color: #ffffff; padding:20px; border-radius:15px; 
                          box-shadow:0px 4px 8px rgba(0,0,0,0.1);}
    </style>
    """, unsafe_allow_html=True
)

st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a customer is likely to churn based on their details.")

# ===========================
# Tabs for Prediction & Info
# ===========================
tab1, tab2 = st.tabs(["🔮 Predict Churn", "📈 About Project"])

# ===========================
# Tab 1 - Prediction Interface
# ===========================
with tab1:
    st.subheader("Enter Customer Details:")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Has Partner", ["Yes", "No"])
        dependents = st.selectbox("Has Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (Months)", 0, 72, 12)

    with col2:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

    with col3:
        device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
        tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method = st.selectbox(
            "Payment Method", 
            ["Electronic check", "Mailed check", 
             "Bank transfer (automatic)", "Credit card (automatic)"]
        )

    monthly_charges = st.slider("Monthly Charges ($)", 0, 120, 50)
    total_charges = st.slider("Total Charges ($)", 0, 8000, 1000)

    # Prediction Button
    if st.button("🔮 Predict Churn"):
        # Prepare input as DataFrame
        input_df = pd.DataFrame([{
            'gender': gender,
            'SeniorCitizen': senior,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone_service,
            'MultipleLines': multiple_lines,
            'InternetService': internet_service,
            'OnlineSecurity': online_security,
            'OnlineBackup': online_backup,
            'DeviceProtection': device_protection,
            'TechSupport': tech_support,
            'StreamingTV': streaming_tv,
            'StreamingMovies': streaming_movies,
            'Contract': contract,
            'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges
        }])

        # Predict
        prob = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        # Display Result in a Card
        st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
        st.subheader("Prediction Result:")
        if pred == 1:
            st.error(f"⚠️ The customer is likely to CHURN.\n\nProbability: **{prob:.2%}**")
        else:
            st.success(f"✅ The customer is NOT likely to churn.\n\nProbability: **{prob:.2%}**")
        st.markdown("</div>", unsafe_allow_html=True)

# ===========================
# Tab 2 - Project Info
# ===========================
with tab2:
    st.subheader("Project Overview")
    st.markdown("""
    This Customer Churn Prediction tool was built using:
    - **EDA & Data Preprocessing:** Pandas, Seaborn
    - **Machine Learning Models:** Logistic Regression, RandomForest, XGBoost
    - **Model Tuning:** GridSearchCV & RandomizedSearchCV for best performance
    - **Deployment:** Streamlit

    **Goal:** Help businesses identify high-risk customers and take action to reduce churn.
    """)
