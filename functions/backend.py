import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Function to load data
def load_data(file_path='pricingdata_cleaned.csv'):
    """
    Load data from a CSV file.
    
    :param file_path: str, the path to the CSV file (default is 'pricingdata_cleaned.csv').
    :return: DataFrame, the loaded data.
    """
    data = pd.read_csv(file_path='pricingdata_cleaned.csv')
    return data