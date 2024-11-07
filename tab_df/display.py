# tab_df/display.py

import streamlit as st
from tab_df.logics import get_summary_info, get_column_info

def display_dataframe_overview(df):
    """Display the overview of the DataFrame in Streamlit."""
    st.header("DataFrame")
    
    
    summary_df = get_summary_info(df)
    st.table(summary_df)
    
  
    column_info = get_column_info(df)
    st.table(column_info)
    
    
    st.subheader("Explore Dataframe")
    
    
    num_rows_display = st.slider("Select number of rows to be displayed", min_value=5, max_value=50, value=5)
    
    
    display_logic = st.radio("Exploration Method", options=["Head", "Tail", "Sample"])
    
    
    if display_logic == "Head":
        st.dataframe(df.head(num_rows_display))
    elif display_logic == "Tail":
        st.dataframe(df.tail(num_rows_display))
    else:
        st.dataframe(df.sample(num_rows_display))

