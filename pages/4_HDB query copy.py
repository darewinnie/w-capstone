import pandas as pd
import streamlit as st
import json
import openai
from helper_functions import llm  
# Ensure you have the OpenAI function defined here
import tiktoken  
# For token counting

# Load the JSON file
filepath = './data/resaleoct23.json'
with open(filepath, 'r') as file:
    dict_of_hdb = json.load(file)

def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def hdb_json(user_message):
    delimiter = "####"
    
    system_message = f"""
    You will be provided with customer service queries about HDB town and resale price from October 2023 to October 2024. 
    The customer service query will be enclosed in the pair of {delimiter}.
    Please provide answers based on the provided data. 
    Please note: "2024-10" means October 2024. 
    Your response must start with Ans: 
    """

    # Prepare the messages
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    # Check the token count and chunk if necessary
    total_tokens = count_tokens(system_message) + count_tokens(user_message)
    
    # Define a chunk size (example: max 3000 tokens)
    max_chunk_size = 3000
    
    if total_tokens > max_chunk_size:
        # Chunk the data
        chunk_size = 100  # Adjust based on your data structure
        chunks = [dict_of_hdb[i:i + chunk_size] for i in range(0, len(dict_of_hdb), chunk_size)]
        
        responses = []
        for chunk in chunks:
            # Convert chunk back to string if needed
            chunk_data = json.dumps(chunk)  # or however you need to format it
            messages.append({'role': 'assistant', 'content': chunk_data})

            # Call the API with the chunk
            hdb_response = llm.get_completion_by_messages(messages)
            responses.append(hdb_response)
        
        return " ".join(responses)  # Combine responses
    else:
        # If under limit, proceed as normal
        return llm.get_completion_by_messages(messages)

# Streamlit UI
st.title("HDB Resale Price Chatbot")

# Input for user queries
user_input = st.text_input("Ask a question about HDB towns and resale prices:")

if st.button("Get Answer"):
    if user_input:
        # Get the response from the model
        response = hdb_json(user_input)
        
        # Display the response
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please enter a query.")