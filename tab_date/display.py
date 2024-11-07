import streamlit as st
import altair as alt
import pandas as pd
from tab_date.logics import calculate_date_stats, get_top_20_frequent_dates

def display_date_series_analysis(df):
    """Display the date series analysis in Streamlit."""
    st.header("Date Series Analysis")
    
   
    datetime_columns = df.select_dtypes(include=['datetime']).columns.tolist()
    if not datetime_columns:
        text_columns = df.select_dtypes(include=['object']).columns.tolist()
        datetime_columns = text_columns
    
    if datetime_columns:
        
        selected_column = st.selectbox("Select a datetime column for analysis:", datetime_columns)
        
        if selected_column:
           
            df[selected_column] = pd.to_datetime(df[selected_column], errors='coerce')
            col_data = df[selected_column].dropna()
            
            
            stats_df = calculate_date_stats(col_data)
            st.table(stats_df)
            
            
            histogram = alt.Chart(col_data.to_frame()).mark_bar().encode(
                alt.X(selected_column + ":T", timeUnit='yearmonth'),
                y='count()'
            ).properties(
                width=600,
                height=400,
                title=f"Distribution of {selected_column}"
            )
            st.altair_chart(histogram, use_container_width=True)
            
            
            top_20_dates = get_top_20_frequent_dates(col_data)
            st.write("Top 20 Most Frequent Dates:")
            st.dataframe(top_20_dates)
    else:
        st.warning("No datetime or text columns found in the dataset.")
