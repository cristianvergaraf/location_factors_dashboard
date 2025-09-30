import streamlit as st 
import pandas as pd
from src.definitions import variables_to_select
from src.viz_helpers import interactive_scatter

# Page config
st.set_page_config(layout = "wide")

# Read data
data = pd.read_csv(r"data/results_all_models_with_number_of_variables.csv")

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


interactive_scatter(data,x_variable_plot1,y_variable_plot1)

st.title("COMPARE BETWEEN MODELS")

col3, col4 = st.columns(2)

with col3:
    default_index = variables_to_select.index("toc_auc") if "toc_auc" in variables_to_select else 0
    x_variable_plot_2 = st.selectbox(
        "Select variable for x axis",
        variables_to_select,
        index  = default_index

    )
    

with col4:
    default_index = variables_to_select.index("aic") if "aic" in variables_to_select else 0
    y_variable_plot_2 = st.selectbox(
        "Select variable for y axis",
        variables_to_select,
        index  = default_index

    )


interactive_scatter(data,x_variable_plot_2,y_variable_plot_2)

st.title("Spatial validation of logistic models to predict forest plantation expansion in the lingue basin")
st.dataframe(data)