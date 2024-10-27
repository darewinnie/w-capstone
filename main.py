# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler_copy import hdb_json
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="HDB Resale Price Finder"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("HDB Resale Price Finder")

form = st.form(key="form")
form.subheader("Please ask me about recent hdb resale data")

user_prompt = form.text_area("You may ask what is the average price of 4 room in Ang Mo Kio town", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    hdb_response = hdb_json_2(user_prompt)
    st.write(hdb_response)

with st.expander("Disclaimer"):
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalized advice.")