import streamlit as st 
import numpy as np
import pandas as pd
from src.definitions import variables_to_select
from src.viz_helpers import interactive_scatter

#import statsmodels.formula.api as smf

import copy

st.set_page_config(layout = "wide")

# Read data

data = pd.read_csv(r"data/results_all_models.csv")

st.title("RELATIVE IMPORTANCE OF RELATIVE FACTOR LINGUE BASIN. SOUTH CENTRAL CHILE")
st.dataframe(data)


st.title("INTERACTIVE SCATTERPLOT")

col1, col2 = st.columns(2)

with col1:
    x_variable = st.selectbox(
        "Select variable for x axis",
        variables_to_select

    )
    

with col2:
    y_variable = st.selectbox(
        "How would you like to be contacted?",
        variables_to_select
        
    )


interactive_scatter(data,x_variable,y_variable,"model_id")



