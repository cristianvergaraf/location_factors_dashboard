import streamlit as st 
import pandas as pd
from src.definitions import variables_to_select
from src.viz_helpers import interactive_scatter
from src.load_helpers import load_data

# Page config
st.set_page_config(layout = "wide")

# Read data
data = load_data(r"data/results_all_models_with_number_of_variables.csv")

st.title("INTERACTIVE SCATTERPLOT")

col1, col2 = st.columns(2)



with col1:
    default_index = variables_to_select.index("aic") if "aic" in variables_to_select else 0
    x_variable_plot1 = st.selectbox(
        "Select variable for x axis",
        variables_to_select,
        index = default_index

    )
    
with col2:
    default_index = variables_to_select.index("fom") if "fom" in variables_to_select else 0
    y_variable_plot1 = st.selectbox(
        "Select variable for y axis",
        variables_to_select,
        index = default_index

    )

def calculate_range_slider(variable):
    """
    Calculate the min and max values for the range slider based on the range of the selected variable.
    """
    min_value = data[variable].min()
    max_value = data[variable].max()

    return min_value, max_value

min_value, max_value = calculate_range_slider(x_variable_plot1)

values = st.slider("Select a range of values", min_value, max_value, (min_value, max_value))



def filter_data(variable:str, value_range:tuple):
    """
    Filter the DataFrame based on the selected variable and value range.
    """
    filtered_data = data[(data[variable] >= value_range[0]) & (data[variable] <= value_range[1])]
    return filtered_data

filtered_data = filter_data(x_variable_plot1, values)   

def update_interactive_plot_based_on_filters(filtered_data, x_variable_plot1, y_variable_plot1):
    """
    Update the interactive plot based on the selected filters.
    
    """
    return interactive_scatter(filtered_data, x_variable_plot1, y_variable_plot1)

def reset_filters():
    """
    Reset the filters to show the original DataFrame.
    """
    return data

# Initialization

if 'x_variable_plot1' not in st.session_state:
    st.session_state['x_variable_plot1'] = x_variable_plot1

if 'y_variable_plot1' not in st.session_state:
    st.session_state['y_variable_plot1'] = y_variable_plot1

if st.button("Update session state"):
    st.session_state['x_variable_plot1'] = x_variable_plot1
    st.session_state['y_variable_plot1'] = y_variable_plot1


interactive_scatter(data,st.session_state['x_variable_plot1'],st.session_state['y_variable_plot1'])
st.title("COMPARE BETWEEN MODELS")

col3, col4 = st.columns(2)

with col3:
    default_index = variables_to_select.index("toc_auc") if "toc_auc" in variables_to_select else 0
    x_variable_plot2 = st.selectbox(
        "Select variable for x axis",
        variables_to_select,
        index  = default_index

    )
    

with col4:
    default_index = variables_to_select.index("aic") if "aic" in variables_to_select else 0
    y_variable_plot2 = st.selectbox(
        "Select variable for y axis",
        variables_to_select,
        index  = default_index

    )

if 'x_variable_plot2' not in st.session_state:
    st.session_state['x_variable_plot2'] = x_variable_plot2

if 'y_variable_plot2' not in st.session_state:
    st.session_state['y_variable_plot2'] = y_variable_plot2

if st.button("Update session state for plot 2"):
    st.session_state['x_variable_plot2'] = x_variable_plot2
    st.session_state['y_variable_plot2'] = y_variable_plot2
   


interactive_scatter(filtered_data,x_variable_plot2,y_variable_plot2)


# Creamos dos elementos dentro de session state

if "df" not in st.session_state:
    st.session_state.df = data

# if 'selected_df' not in st.session_state:
#     st.session_state.edited_df = selected_df

# I want 


st.title("Spatial validation of logistic models to predict forest plantation expansion in the lingue basin")
st.dataframe(data)