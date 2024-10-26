import streamlit as st

# Page configuration
st.set_page_config(page_title="Loan Eligibility Checker", layout="centered")
st.title("Loan Eligibility Checker")
st.write("Find out if you're eligible for a loan with a quick check.")

# Input fields for loan eligibility criteria
with st.form("loan_form"):
    age = st.slider("Age", 18, 70, 30)
    income = st.number_input("Monthly Income (in ₹)", min_value=0, value=50000, step=500)
    employment_status = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
    credit_score = st.slider("Credit Score", 300, 850, 700)
    existing_debts = st.number_input("Total Existing Monthly Debts (in ₹)", min_value=0, value=0, step=500)
    loan_amount = st.number_input("Loan Amount Requested (in ₹)", min_value=10000, value=100000, step=10000)
    loan_term_years = st.number_input("Loan Term (in years)", min_value=1, max_value=30, value=5)
    
    # Submit button
    submitted = st.form_submit_button("Check Eligibility")

# Loan eligibility criteria function
def check_loan_eligibility(age, income, employment_status, credit_score, existing_debts, loan_amount, loan_term_years):
    # Parameters for loan eligibility
    min_age, max_age = 21, 65
    min_credit_score = 650
    max_dti_ratio = 0.4  # Debt-to-Income ratio threshold (40%)

    # Basic eligibility checks
    if age < min_age or age > max_age:
        return False, "Applicant age must be between 21 and 65 years."
    if employment_status == "Unemployed":
        return False, "Applicant must be employed or self-employed."
    if credit_score < min_credit_score:
        return False, "A minimum credit score of 650 is required."
    
    # Calculate monthly payment and Debt-to-Income (DTI) ratio
    monthly_payment = loan_amount / (loan_term_years * 12)
    dti_ratio = (existing_debts + monthly_payment) / income

    if dti_ratio > max_dti_ratio:
        return False, f"Debt-to-Income (DTI) ratio exceeds {max_dti_ratio * 100}%. Reduce existing debts or increase income."

    # Eligibility confirmed
    return True, f"You are eligible for the loan. Estimated monthly payment: ₹{monthly_payment:,.2f}"

# Eligibility check and result display
if submitted:
    is_eligible, message = check_loan_eligibility(age, income, employment_status, credit_score, existing_debts, loan_amount, loan_term_years)
    if is_eligible:
        st.success(message)
    else:
        st.error(message)
