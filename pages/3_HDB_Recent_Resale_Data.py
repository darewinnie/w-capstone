import pandas as pd
import streamlit as st

#Read CSV file from file
df = pd.read_csv('./data/resaleoct23.csv')

#Print CSV table
st.title("HDB Recent Resale Data 🏠")  # add a title
st.write(df)

# Add filters
st.sidebar.header("Filters")

# Filter by town
towns = df['town'].unique()  # Adjust 'town' to your column name
selected_town = st.sidebar.selectbox("Select Town", options=["All"] + list(towns))

# Filter by flat type
flat_types = df['flat_type'].unique()  # Adjust 'flat_type' to your column name
selected_flat_type = st.sidebar.selectbox("Select Flat Type", options=["All"] + list(flat_types))

# Filter by price range
min_price = int(df['resale_price'].min())  # Adjust 'price' to your column name
max_price = int(df['resale_price'].max())
selected_price_range = st.sidebar.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price))

# Apply filters
filtered_df = df.copy()
    
if selected_town != "All":
        filtered_df = filtered_df[filtered_df['town'] == selected_town]

if selected_flat_type != "All":
        filtered_df = filtered_df[filtered_df['flat_type'] == selected_flat_type]

filtered_df = filtered_df[(filtered_df['resale_price'] >= selected_price_range[0]) & (filtered_df['resale_price'] <= selected_price_range[1])]

# Display the filtered DataFrame
st.subheader("Filtered Data")
st.write(filtered_df)
