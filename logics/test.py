import pandas as pd
import streamlit as st
import os
import json
import openai
from helper_functions import llm
import lolviz

# Load the JSON file
filepath = './data/resaleoct23.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_hdb = json.loads(json_string)
    
lolviz.objviz(dict_of_hdb)

