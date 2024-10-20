import streamlit as st
import pandas as pd


st.title("HDB Loan Repayment Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)
hdb_value = col1.number_input("HDB Resale Price", min_value=0, value=600000)
downpayment = col1.number_input("Downpayment (25% of Resale Price)", min_value=0, value=150000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=2.6)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# Calculate the repayments.
loan_amount = hdb_value - downpayment
monthly_interest_rate = (interest_rate / 100) / 12
number_of_installment = loan_term * 12
monthly_installment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_installment)
    / ((1 + monthly_interest_rate) ** number_of_installment - 1)
)

# Display the repayments.
total_payments = monthly_installment * number_of_installment
total_interest = total_payments - loan_amount

st.write("### Loan Payment")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Installment", value=f"${monthly_installment:,.2f}")
col2.metric(label="Total Payment", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

