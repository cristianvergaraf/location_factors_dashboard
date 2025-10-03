import streamlit as st

def update_state(edit):
    st.session_state.edited_df = edit

def update_df(new_df):
    st.session_state['edited_df'] = new_df


#def update_interactive_plot_based_on_filters(filtered_data, x_variable_plot1, y_variable_plot1):
    """
    Update the interactive plot based on the selected filters.
    
    """
    #return interactive_scatter(filtered_data, x_variable_plot1, y_variable_plot1)

def reset_filters():
    """
    Reset the filters to show the original DataFrame.
    """
    #return data
