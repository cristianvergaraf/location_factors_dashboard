
import plotly.express as px 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

    
def interactive_scatter(df,x_axis,y_axis):
    # Custom color palette
   # custom_palette = ["red", "green", "blue", "black", "gray"]

    # Ensure categorical
    hover_columns = ["model_id","variables"]


    # Create the scatter plot
    scatter_fig = px.scatter(
        data_frame=df,
        x=x_axis,
        y=y_axis,
        #color = metric,
        #color_discrete_map={value: color for value, color in zip(df[metric].unique(), custom_palette)},
        labels={'variable': ' ', 'value': 'Factor value'},
        title='Fig 1. Media de cada variable para cada cluster',
        width=1000,
        height=500,
        hover_data = hover_columns
    )

    # Config for toolbar
    config = {"displaylogo": False, "responsive": True}

    # Layout: center chart
    left, center, right = st.columns([1, 4, 1])  # adjust ratio as needed
    with center:
        st.plotly_chart(scatter_fig, use_container_width=True, config=config)
