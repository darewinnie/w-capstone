import pandas as pd
import streamlit as st

#Read CSV file from file
df = pd.read_csv('./data/resaleoct23.csv')

#Print CSV table
st.title("HDB Resale Data ")  # add a title
st.write(df)

df = get_data()


month = df['month'].unique()

'# By town'
town = st.selectbox('town', town)
df[df['town'] == town]

