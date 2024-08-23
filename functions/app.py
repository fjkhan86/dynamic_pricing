import streamlit as st
import pandas as pd

# Load data function
def load_data(file_path):
    return pd.read_csv(file_path)

# Streamlit app
st.title("DataFrame Loader in Streamlit")

# Path to your CSV file
data_path = '/mnt/data/pricingdata_cleaned.csv'  # Use the correct path based on your environment

# Load the DataFrame
df = load_data(data_path)
