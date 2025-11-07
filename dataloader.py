#importing pandas for data handling
import pandas as pd

#importing os for file path operations
import os

# Defining the path to the CSV file
DATA_PATH = "../data/player_history.csv"

# Function to load data from CSV file
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        # Create empty DataFrame with columns if no CSV exists
        return pd.DataFrame(columns=["num1","num2","user_answer","correct","time_taken"])

# Function to save data to CSV file
def save_data(df):
    df.to_csv(DATA_PATH, index=False)