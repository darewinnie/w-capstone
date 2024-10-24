import pandas as pd
import streamlit as st
import os
import json
import openai
from helper_functions import llm

# Load the JSON file
filepath = './data/resale.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_hdb = json.loads(json_string)


def hdb_json(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries about hdb town and resale price . \
    Please answer based on the JSON file. \
    Please remember you have data for October 2023, November 2023, December 2023, January 2024, February 2024, March 2024, April 2024, May 2024, June 2024, July 2024, August 2024, September 2024 and October 2024 as "month": "2024-10" refer to October 2024 \
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
    