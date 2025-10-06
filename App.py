import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)

st.write("# Welcome to locations factors dashboard ! 👋")

st.markdown(
    """
    This dashboard shows the results of tha analysis of location factors of forest plantations in the Lingue basin 
    in south-central Chile. The analysis was perfomed using a multimodel inference approach (Burnham and Anderson, 2004) implemented using the 
    glmulti package in R, to compute all the possible models with 10 variables, 1024 models in total. Then, spatial predictions where 
    perfomed using Terra package using the predict functions. Metrics of model fitness as AIC, AUC,
    and spatial predictions were calculated, including AUC, TOC, FOM.

    - Checkout the repository of the projects in github [documentation](https://github.com/cristianvergaraf/location_factors)

    """ 
       
)
