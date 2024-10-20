import pandas as pd
import streamlit as st

#Read CSV file from file
df = pd.read_csv('./data/resaleoct23.csv')

#Print CSV table
st.title("HDB Resale Data Since Oct 2023")  # add a title
st.write(df)