#######################################################################
# Yi Jin Toh
# 09/19/2024
# This script contains helper functions for cleaning data
#######################################################################

# import packages
import pandas as pd

# set paths to data
sales_data = '../data/sales.xlsx'
temp_data = '../data/temp.xlsx'

# Function to read data and return all valid dates and values
def get_cleaned_data(data_path):
    """
    Args:
        data_path (str):    Path to data 
    Returns:
        pd.DataFrame:       Data in the form of a Pandas dataframe,
                            with NaN entries dropped.
    """
    return pd.read_excel(data_path).dropna() #.reset_index(drop=True)