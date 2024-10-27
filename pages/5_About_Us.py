import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us")

st.header("Project Scope")

st.write("The application is for users to check out on past HDB resale data based on different categories (Eg. unit type, location, transaction year etc) to facilitate users to look for suitable HDB flat based on their budget.")

st.header("Objective")

st.write("1. Help user look for past hdb resale data easily using chatbot")
st.write("2. Help user to estimate budget requirement such as downpayment and monthly installment using calculator")