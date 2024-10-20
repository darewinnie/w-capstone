from bs4 import BeautifulSoup
import requests
import os
import json
import openai
from helper_functions import llm

url = "https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/overview"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

final_text = soup.text.replace('\n', '')

len(final_text.split())