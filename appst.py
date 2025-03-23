import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("Handwritten numbers")
st.write("this is my new app")

#Streamlit design
# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Change main background */
        .stApp {
            background-color: #cce7ff;
        }

        /* Style the sidebar */
        section[data-testid="stSidebar"] {
            background-color: #99c2ff;
        }

        /* Style buttons */
        .stButton > button {
            background-color: orange !important;
            color: black !important;
            font-size: 18px;
        }

        .stButton > button:hover {
            background-color: #e69500 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Upload Picture", "Use Camera to Load"])

# Page Content Based on Selection
if selection == "Upload Picture":
    st.title("Upload Picture")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

elif selection == "Use Camera to Load":
    st.title("Use Camera to Load")
    camera_image = st.camera_input("Take a picture")
    if camera_image is not None:
        st.image(camera_image, caption="Captured Image", use_column_width=True)
