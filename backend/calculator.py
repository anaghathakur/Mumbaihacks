import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title for the Streamlit App
st.title("Financial Calculators and Simulators in INR")

# 1. Savings Goal Calculator
st.header("Savings Goal Calculator")
goal_amount = st.number_input("Savings Goal Amount (₹)", min_value=0.0, step=1000.0, key="goal_amount")
years_to_goal = st.number_input("Years to Achieve Goal", min_value=1, step=1, key="years_to_goal")
interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, step=0.1, key="interest_rate")

if st.button("Calculate Monthly Contribution for Savings Goal"):
    monthly_rate = (interest_rate / 100) / 12
    months = years_to_goal * 12
    if monthly_rate == 0:
        monthly_contribution = goal_amount / months
    else:
        monthly_contribution = goal_amount * monthly_rate / ((1 + monthly_rate) ** months - 1)
    st.write(f"Monthly Contribution Needed: ₹{monthly_contribution:.2f}")
    
    # Plotting the savings accumulation over time
    savings = [monthly_contribution * ((1 + monthly_rate) ** i - 1) / monthly_rate for i in range(1, months + 1)]
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, months + 1), savings, label="Accumulated Savings", color="blue")
    plt.xlabel("Months")
    plt.ylabel("Accumulated Savings (₹)")
    plt.title("Savings Accumulation Over Time")
    plt.legend()
    st.pyplot(plt)

# 2. Loan Repayment Calculator
st.header("Loan Repayment Calculator")
principal_amount = st.number_input("Loan Amount (₹)", min_value=0.0, step=1000.0, key="principal_amount")
loan_duration = st.number_input("Loan Duration (years)", min_value=1, step=1, key="loan_duration")
loan_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, step=0.1, key="loan_interest_rate")

if st.button("Calculate Monthly Loan Payment"):
    monthly_loan_rate = (loan_interest_rate / 100) / 12
    loan_months = loan_duration * 12
    if monthly_loan_rate == 0:
        monthly_payment = principal_amount / loan_months
    else:
        monthly_payment = principal_amount * monthly_loan_rate / (1 - (1 + monthly_loan_rate) ** -loan_months)
    st.write(f"Monthly Loan Payment: ₹{monthly_payment:.2f}")

    # Plotting the loan balance over time
    loan_balance = [principal_amount * ((1 + monthly_loan_rate) ** i - (1 + monthly_loan_rate) ** (i - loan_months)) / monthly_loan_rate for i in range(1, loan_months + 1)]
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, loan_months + 1), loan_balance, label="Remaining Loan Balance", color="red")
    plt.xlabel("Months")
    plt.ylabel("Remaining Loan Balance (₹)")
    plt.title("Loan Repayment Balance Over Time")
    plt.legend()
    st.pyplot(plt)

# 3. Investment Growth Simulator
st.header("Investment Growth Simulator")
initial_investment = st.number_input("Initial Investment (₹)", min_value=0.0, step=1000.0, key="initial_investment")
annual_return_rate = st.number_input("Expected Annual Return Rate (%)", min_value=0.0, max_value=100.0, step=0.1, key="annual_return_rate")
investment_duration = st.number_input("Investment Duration (years)", min_value=1, step=1, key="investment_duration")

if st.button("Simulate Investment Growth"):
    future_value = initial_investment * (1 + annual_return_rate / 100) ** investment_duration
    st.write(f"Estimated Investment Value after {investment_duration} years: ₹{future_value:.2f}")

    # Plotting the investment growth
    growth = [initial_investment * (1 + annual_return_rate / 100) ** i for i in range(investment_duration + 1)]
    plt.figure(figsize=(10, 5))
    plt.plot(range(0, investment_duration + 1), growth, label="Investment Growth", color="green")
    plt.xlabel("Years")
    plt.ylabel("Investment Value (₹)")
    plt.title("Investment Growth Over Time")
    plt.legend()
    st.pyplot(plt)

# 4. Retirement Planning Calculator
st.header("Retirement Planning Calculator")
annual_expenses_in_retirement = st.number_input("Expected Annual Expenses in Retirement (₹)", min_value=0.0, step=1000.0, key="annual_expenses_in_retirement")
retirement_years = st.number_input("Years in Retirement", min_value=1, step=1, key="retirement_years")
retirement_interest_rate = st.number_input("Expected Annual Return Rate in Retirement (%)", min_value=0.0, max_value=100.0, step=0.1, key="retirement_interest_rate")

if st.button("Calculate Retirement Savings Needed"):
    retirement_rate = retirement_interest_rate / 100
    if retirement_rate == 0:
        retirement_savings_needed = annual_expenses_in_retirement * retirement_years
    else:
        retirement_savings_needed = annual_expenses_in_retirement * ((1 - (1 + retirement_rate) ** -retirement_years) / retirement_rate)
    st.write(f"Total Savings Needed for Retirement: ₹{retirement_savings_needed:.2f}")

    # Plotting retirement savings depletion over time
    savings_depletion = [retirement_savings_needed * (1 + retirement_rate) ** i - annual_expenses_in_retirement * ((1 + retirement_rate) ** i - 1) / retirement_rate for i in range(1, retirement_years + 1)]
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, retirement_years + 1), savings_depletion, label="Retirement Savings Depletion", color="purple")
    plt.xlabel("Years in Retirement")
    plt.ylabel("Remaining Savings (₹)")
    plt.title("Retirement Savings Over Time")
    plt.legend()
    st.pyplot(plt)
