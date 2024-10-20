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


def hdb_json(user_input):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_input}{delimiter}"},
    ]
    hdb_response_str = llm.get_completion_by_messages(messages)
    hdb_response_str = hdb_response_str.replace("'", "\"")
    hdb_response = json.loads(hdb_response_str)
    return hdb_response
    
    