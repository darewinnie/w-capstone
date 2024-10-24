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
    dict_of_hdb = json.loads(json_string)


def hdb_json(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries about hdb town and resale price from october 2023 to october 2024. \
    Please answer based on the json file. \
    Please note that month": "2024-09" refer to september 2024, 2024-10 refer to october 2024\     
    Your response must start with Ans: \
    
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    hdb_response = llm.get_completion_by_messages(messages)
   
    return hdb_response
    