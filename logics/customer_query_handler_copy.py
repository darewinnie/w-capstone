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
    Please take note:
    
    "month": " month of the year",
    "town": "town in Singapore for the resale flat",
    "flat_type": "type of resale flat",
    "block": "block name or number of the resale flat",
    "street_name": "street name of the resale flat",
    "storey_range": "range of storey for the resale flat",
    "floor_area_sqm": "total floor area of the resale flat",
    "flat_model": "type of flat model",
    "lease_commence_date": "year of lease of commencement of the resal flat",
    "remaining_lease": "73 years 07 months",
    "resale_price": "amount of resale price", \

    
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
    