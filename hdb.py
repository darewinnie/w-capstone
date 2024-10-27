import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
import tiktoken
from helper_functions import llm

def fetch_url_content(url):
    """Fetch content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text from paragraphs
        return ' '.join([p.get_text() for p in soup.find_all('p')])
    except requests.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
        return None

def count_tokens(text, model="gpt-4"):
    """Count the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def get_openai_response(prompt):
    """Get a response from OpenAI's API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the preferred model
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error communicating with OpenAI: {e}")
        return None

# Streamlit UI
st.title("OpenAI Chatbot from Web Content")

# Input for URL
url = st.text_input("Enter the URL of the website you want to fetch content from:")

if st.button("Fetch Content"):
    if url:
        content = fetch_url_content(url)
        if content:
            st.subheader("Fetched Content")
            st.write(content[:500] + "...")  # Display the first 500 characters
            st.session_state['fetched_content'] = content
        else:
            st.warning("Failed to fetch content from the provided URL.")
    else:
        st.warning("Please enter a valid URL.")

if 'fetched_content' in st.session_state:
    user_input = st.text_input("Ask a question based on the fetched content:")
    
    if st.button("Get Answer"):
        if user_input:
            prompt = f"Based on the following content, answer the question:\n\n{st.session_state['fetched_content']}\n\nQuestion: {user_input}"
            
            # Check token limit
            if count_tokens(prompt) > 4000:  # Adjust based on model limits
                st.warning("The request is too large. Please ask a more specific question.")
            else:
                response = get_openai_response(prompt)
                if response:
                    st.subheader("OpenAI Response")
                    st.write(response)
        else:
            st.warning("Please enter a question.")
else:
    st.warning("Please fetch content from a URL first.")