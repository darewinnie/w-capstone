# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_functions import llm
from logics.hdb_json_query import hdb_json_2
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
form.subheader("Please ask me")

user_prompt = form.text_area("You may ask what is the average price of 4 room in Ang Mo Kio town", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    hdb_response = hdb_json_2(user_prompt)
    st.write(hdb_response)
