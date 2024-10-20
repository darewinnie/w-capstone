import pandas as pd
import streamlit as st
import os
import json
import openai
from helper_functions import llm

# Load the JSON file
filepath = './data/resaleoct23.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)


def hdb_json(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    hdb_response = llm.get_completion_by_messages(messages)
   
    return hdb_response
    