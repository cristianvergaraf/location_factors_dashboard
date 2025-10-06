import streamlit as st 
import pandas as pd
from src.definitions import variables_to_select
from src.viz_helpers import interactive_scatter
from src.load_helpers import load_data
from src.utils import filter_data, compute_range, calculate_range_slider

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


min_value, max_value = calculate_range_slider(data, x_variable_plot1)

values = st.slider("Select a range of values", min_value, max_value, (min_value, max_value))

filtered_data = filter_data(data, x_variable_plot1, values)

original_x_range, original_y_range = compute_range(data, x_variable_plot1, y_variable_plot1)

Number_of_models = filtered_data.shape[0]


# Initialization

if 'x_variable_plot1' not in st.session_state:
    st.session_state['x_variable_plot1'] = x_variable_plot1

if 'y_variable_plot1' not in st.session_state:
    st.session_state['y_variable_plot1'] = y_variable_plot1

if st.button("Update models in the filtered data"):
    st.session_state['x_variable_plot1'] = x_variable_plot1
    st.session_state['y_variable_plot1'] = y_variable_plot1


interactive_scatter(data,st.session_state['x_variable_plot1'],st.session_state['y_variable_plot1'], key = "original_plot")

st.metric(label="Number of models in the filtered data", value=Number_of_models)

interactive_scatter(filtered_data,st.session_state['x_variable_plot1'],st.session_state['y_variable_plot1'],range_x=original_x_range, range_y=original_y_range, key = "filtered_plot")



# st.title("COMPARE BETWEEN MODELS")


# col3, col4 = st.columns(2)

# with col3:
#     default_index = variables_to_select.index("toc_auc") if "toc_auc" in variables_to_select else 0
#     x_variable_plot2 = st.selectbox(
#         "Select variable for x axis",
#         variables_to_select,
#         index  = default_index

#     )
    

# with col4:
#     default_index = variables_to_select.index("aic") if "aic" in variables_to_select else 0
#     y_variable_plot2 = st.selectbox(
#         "Select variable for y axis",
#         variables_to_select,
#         index  = default_index

#     )

# if 'x_variable_plot2' not in st.session_state:
#     st.session_state['x_variable_plot2'] = x_variable_plot2

# if 'y_variable_plot2' not in st.session_state:
#     st.session_state['y_variable_plot2'] = y_variable_plot2

# if st.button("Update session state for plot 2"):
#     st.session_state['x_variable_plot2'] = x_variable_plot2
#     st.session_state['y_variable_plot2'] = y_variable_plot2
   


# interactive_scatter(filtered_data,x_variable_plot2,y_variable_plot2)


# # Creamos dos elementos dentro de session state

# if "df" not in st.session_state:
#     st.session_state.df = data

# # if 'selected_df' not in st.session_state:
# #     st.session_state.edited_df = selected_df

# # I want 


# st.title("Spatial validation of logistic models to predict forest plantation expansion in the lingue basin")
# st.dataframe(data)
