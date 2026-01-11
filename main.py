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
# SOFT LIGHT FINTECH THEME
# --------------------------------------------------
st.markdown("""
<style>

/* Soft gradient background */
.stApp {
    background: linear-gradient(120deg, #f8fafc, #eef2ff);
    color: #0f172a;
}

/* Page title */
h1 {
    font-weight: 700;
    color: #0f172a;
}

/* Section title */
h3 {
    color: #1e293b;
    margin-bottom: 14px;
}

/* Card container */
.card {
    background-color: #ffffff;
    padding: 26px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 24px rgba(0,0,0,0.06);
    margin-bottom: 24px;
}

/* Labels */
label {
    font-size: 14px !important;
    color: #334155 !important;
}

/* Inputs */
div[data-baseweb="input"] input,
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border-radius: 10px !important;
    border: 1px solid #c7d2fe !important;
    color: #0f172a !important;
}

/* Disabled input */
input:disabled {
    background-color: #f1f5f9 !important;
    font-weight: 600;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #3b82f6);
    color: white;
    font-size: 16px;
    font-weight: 600;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #4f46e5, #2563eb);
    transform: scale(1.03);
}

/* Result cards */
.result-card {
    background: #ffffff;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    text-align: center;
}

.result-label {
    font-size: 14px;
    color: #64748b;
}

.result-value {
    font-size: 30px;
    font-weight: 700;
    color: #2563eb;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📊 Lauki Finance – Credit Risk Modelling")
st.markdown("##### Intelligent Credit Scoring & Default Risk Assessment")

# --------------------------------------------------
# INPUT CARD
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🧾 Applicant & Loan Information")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, value=28)

with row1[1]:
    income = st.number_input("Annual Income", min_value=0, value=1_200_000)

with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=100_000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.number_input(
        "Loan to Income Ratio",
        value=round(loan_to_income_ratio, 2),
        disabled=True
    )

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

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# ACTION
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Calculate Credit Risk"):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📈 Risk Assessment Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Default Probability</div>
                <div class="result-value">{probability:.2%}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Credit Score</div>
                <div class="result-value">{credit_score}</div>
            </div>
            """, unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Risk Rating</div>
                <div class="result-value">{rating}</div>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
