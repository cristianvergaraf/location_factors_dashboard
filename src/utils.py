import streamlit as st
import pandas as pd

def compute_range(df:pd.DataFrame, x:str, y:str) -> tuple[float,float]:
    """
    Compute the min and max values for a given variable in the DataFrame.
    """
    
    x_range = df[x].min(), df[x].max()
    y_range = df[y].min(), df[y].max()
    
    return x_range, y_range

def filter_data(data:pd.DataFrame, variable:str, value_range:tuple)-> pd.DataFrame:
    """
    Filter the DataFrame based on the selected variable and value range.
    """
    filtered_data = data[(data[variable] >= value_range[0]) & (data[variable] <= value_range[1])]
    return filtered_data


def compute_number_of_rows(data:pd.DataFrame) -> int:
    """
    Compute the number of rows in the DataFrame.
    """
    return data.shape[0]

def calculate_range_slider(data:pd.DataFrame, variable:str) -> tuple[float,float]:
    """
    Calculate the min and max values for the range slider based on the range of the selected variable.
    """
    min_value = data[variable].min()
    max_value = data[variable].max()

    return min_value, max_value


