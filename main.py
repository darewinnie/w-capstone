# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, hdb_response = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    print(hdb_response)
    df = pd.DataFrame(hdb_response)
    df 
