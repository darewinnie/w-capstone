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
st.image(image_path, caption="This is a PNG image", use_column_width=True)

