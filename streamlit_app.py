# streamlit_app.py

# streamlit run "/Users/gregoryjoseph/Desktop/Data Science Practices/Assignment 3/dsp_at3_group32/app/streamlit_app.py"

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd
from tab_df.display import display_dataframe_overview
from tab_numeric.display import display_numeric_series_analysis
from tab_text.display import display_text_series_analysis
from tab_date.display import display_date_series_analysis

st.title("CSV Explorer WebApp")
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs(["DataFrame", "Numeric Series", "Text Series", "Date Series"])
        
        with tab1:
            display_dataframe_overview(df)
        
        with tab2:
            display_numeric_series_analysis(df)
        
        with tab3:
            display_text_series_analysis(df)
        
        with tab4:
            display_date_series_analysis(df)
    
    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty or invalid. Please upload a valid CSV file.")
else:
    st.info("Please upload a CSV file to start the analysis.")
