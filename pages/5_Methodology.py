import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

# Specify the path to your PNG image
image_path = "./data/drawio.png"

# Display the image
st.image(image_path, caption="This is flow chart for 3 functions in the application", use_column_width=True)

st.write (" Please read the readme file in my github depository https://github.com/darewinnie/w-capstone ")

