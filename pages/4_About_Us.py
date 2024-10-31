import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us 🧑‍🤝‍🧑")

st.header("Project Scope")

st.write("The application is for users to check out on recent past HDB resale data based on different categories (Eg. unit type, location, transaction year etc) to facilitate users to look for suitable HDB flat based on their budget.")

st.header("Objectives")

st.write("1. Help user look for recent past HDB resale data easily.")
st.write("2. Help user to estimate budget requirement (eg. downpayment and monthly installment).")
st.write("3. Help user to look for details of recent past HDB resale data. ")

st.header("Data Source")
st.write("Resale flat prices based on registration date from Jan-2017 onwards:https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view.")

st.header("Features")

st.write("1. User Friendly Chatbot - User can enter their query regarding the recent HDB resale data.")
st.write("2. HDB Loan Repayment Calculator -  User can use the calculator to estimate the budget requirement for downpayment and monthly installment requirement based on different interest rate.")
st.write("3. HDB Recnt Resale Data Table - User can look for details of the recent HDB resale by using dropdown and slider filtering function. ")

