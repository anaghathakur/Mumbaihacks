import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for income, expense data, and custom categories
if 'income_entries' not in st.session_state:
    st.session_state['income_entries'] = [{}]
if 'expense_entries' not in st.session_state:
    st.session_state['expense_entries'] = [{}]
if 'custom_income_sources' not in st.session_state:
    st.session_state['custom_income_sources'] = ["Salary", "Investments", "Other"]
if 'custom_expense_categories' not in st.session_state:
    st.session_state['custom_expense_categories'] = ["Fixed", "Variable", "Discretionary"]

# Title and basic settings
st.title("Enhanced Expense Tracker")
st.sidebar.header("Settings")

# Currency Selection
currency = st.sidebar.selectbox("Choose Currency", ("₹ - Rupees", "$ - Dollars"))
currency_symbol = "₹" if currency.startswith("₹") else "$"

# Savings Goal
savings_goal = st.sidebar.number_input("Monthly Savings Goal", min_value=0, value=10000, step=1000)

# Add Custom Income Source
st.sidebar.subheader("Custom Income Source")
new_income_source = st.sidebar.text_input("Add New Income Source")
if st.sidebar.button("Add Income Source"):
    if new_income_source:
        st.session_state['custom_income_sources'].append(new_income_source)
        st.sidebar.success(f"Added new income source: {new_income_source}")

# Add Custom Expense Category
st.sidebar.subheader("Custom Expense Category")
new_expense_category = st.sidebar.text_input("Add New Expense Category")
if st.sidebar.button("Add Expense Category"):
    if new_expense_category:
        st.session_state['custom_expense_categories'].append(new_expense_category)
        st.sidebar.success(f"Added new expense category: {new_expense_category}")

# Income Section
st.header("Add Income")
for i, entry in enumerate(st.session_state['income_entries']):
    st.subheader(f"Income Entry {i+1}")
    entry['source'] = st.selectbox("Income Source", st.session_state['custom_income_sources'], key=f"income_source_{i}")
    entry['amount'] = st.number_input("Amount", min_value=0.0, format="%0.2f", key=f"income_amount_{i}")
    entry['date'] = st.date_input("Date", key=f"income_date_{i}")

if st.button("Add Another Income Entry"):
    st.session_state['income_entries'].append({})

# Save Income Data
if st.button("Save Income Data"):
    if 'income_data' not in st.session_state:
        st.session_state['income_data'] = []
    for entry in st.session_state['income_entries']:
        st.session_state['income_data'].append(entry)
    st.success("Income entries saved.")

# Expense Section
st.header("Add Expenses")
for i, entry in enumerate(st.session_state['expense_entries']):
    st.subheader(f"Expense Entry {i+1}")
    entry['title'] = st.text_input("Expense Title", key=f"expense_title_{i}")
    entry['amount'] = st.number_input("Amount", min_value=0.0, format="%0.2f", key=f"expense_amount_{i}")
    entry['category'] = st.selectbox("Category", st.session_state['custom_expense_categories'], key=f"expense_category_{i}")
    entry['date'] = st.date_input("Date", key=f"expense_date_{i}")

if st.button("Add Another Expense Entry"):
    st.session_state['expense_entries'].append({})

# Save Expense Data
if st.button("Save Expense Data"):
    if 'expense_data' not in st.session_state:
        st.session_state['expense_data'] = []
    for entry in st.session_state['expense_entries']:
        st.session_state['expense_data'].append(entry)
    st.success("Expense entries saved.")

# Summary Section
st.header("Summary")
total_income = sum(entry['amount'] for entry in st.session_state.get('income_data', []))
total_expenses = sum(entry['amount'] for entry in st.session_state.get('expense_data', []))
balance = total_income - total_expenses
spending_percentage = (total_expenses / total_income * 100) if total_income else 0

st.write(f"**Total Income:** {currency_symbol}{total_income:,.2f}")
st.write(f"**Total Expenses:** {currency_symbol}{total_expenses:,.2f}")
st.write(f"**Balance:** {currency_symbol}{balance:,.2f}")
st.write(f"**Spending Percentage:** {spending_percentage:.2f}% of Income")
st.write(f"**Savings Goal:** {currency_symbol}{savings_goal}")

# Visualization: Pie Chart of Expenses by Category
st.header("Expense Breakdown")
expense_df = pd.DataFrame(st.session_state.get('expense_data', []))
if not expense_df.empty:
    expense_summary = expense_df.groupby("category")["amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(expense_summary, labels=expense_summary.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Expenses by Category")
    st.pyplot(fig)
else:
    st.write("No expenses to show.")

# Visualization: Income Trends over Time
st.header("Income Trend")
income_df = pd.DataFrame(st.session_state.get('income_data', []))
if not income_df.empty:
    income_df['date'] = pd.to_datetime(income_df['date'])
    income_df = income_df.sort_values("date")
    fig, ax = plt.subplots()
    ax.plot(income_df['date'], income_df['amount'], marker="o", linestyle="-", color="blue")
    ax.set_title("Income Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Income ({currency_symbol})")
    st.pyplot(fig)
else:
    st.write("No income data to show.")

# Data Reset Option
if st.sidebar.button("Reset All Data"):
    st.session_state.clear()
    st.success("All data reset successfully.")
