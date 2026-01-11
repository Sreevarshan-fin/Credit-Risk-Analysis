import streamlit as st
from prediction_helper import predict

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Lauki Finance | Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS – FINTECH PROFESSIONAL THEME
# --------------------------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
}

/* Title */
h1 {
    color: #f8fafc;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Section headers */
h3 {
    color: #cbd5f5;
    margin-bottom: 10px;
}

/* Input labels */
label {
    color: #cbd5e1 !important;
    font-size: 14px !important;
}

/* Input boxes */
div[data-baseweb="input"] input,
div[data-baseweb="select"] > div {
    background-color: #020617 !important;
    color: #f8fafc !important;
    border-radius: 8px !important;
    border: 1px solid #334155 !important;
}

/* Metric cards */
.metric-card {
    background: linear-gradient(135deg, #020617, #020617);
    border-radius: 14px;
    padding: 20px;
    border: 1px solid #334155;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    text-align: center;
}

/* Metric values */
.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: #38bdf8;
}

/* Metric labels */
.metric-label {
    font-size: 14px;
    color: #94a3b8;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    color: #020617;
    font-size: 16px;
    font-weight: 600;
    padding: 10px 24px;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #1d4ed8, #0ea5e9);
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📊 Lauki Finance – Credit Risk Modelling")
st.markdown("##### Enterprise Credit Scoring & Default Risk Assessment Engine")

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
st.markdown("### 🧾 Applicant & Loan Details")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, value=28)

with row1[1]:
    income = st.number_input("Annual Income", min_value=0, value=1_200_000)

with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=2_560_000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.markdown("**Loan to Income Ratio**")
    st.markdown(f"<div class='metric-value'>{loan_to_income_ratio:.2f}</div>", unsafe_allow_html=True)

with row2[1]:
    loan_tenure_months = st.number_input("Loan Tenure (Months)", min_value=1, value=36)

with row2[2]:
    avg_dpd_per_delinquency = st.number_input("Average DPD", min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input("Delinquency Ratio (%)", min_value=0, max_value=100, value=30)

with row3[1]:
    credit_utilization_ratio = st.number_input("Credit Utilization (%)", min_value=0, max_value=100, value=30)

with row3[2]:
    num_open_accounts = st.number_input("Active Loan Accounts", min_value=1, max_value=10, value=2)

with row4[0]:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])

with row4[1]:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])

with row4[2]:
    loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])

st.divider()

# --------------------------------------------------
# PREDICTION SECTION
# --------------------------------------------------
if st.button("🔍 Calculate Credit Risk"):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("### 📈 Risk Assessment Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Default Probability</div>
                <div class="metric-value">{probability:.2%}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Credit Score</div>
                <div class="metric-value">{credit_score}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Risk Rating</div>
                <div class="metric-value">{rating}</div>
            </div>
            """, unsafe_allow_html=True
        )
