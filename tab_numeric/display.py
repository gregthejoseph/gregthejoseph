
import streamlit as st
import altair as alt
from tab_numeric.logics import calculate_numeric_stats, get_top_20_frequent_values

def display_numeric_series_analysis(df):
    """Display the numeric series analysis in Streamlit."""
    st.header("Numeric Series Analysis")
    
    
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_columns:
        
        selected_column = st.selectbox("Select a numeric column for analysis:", numeric_columns)
        
        if selected_column:
            col_data = df[selected_column]
            
           
            stats_df = calculate_numeric_stats(col_data)
            st.table(stats_df)
            
            
            histogram = alt.Chart(col_data.to_frame()).mark_bar().encode(
                alt.X(selected_column, bin=alt.Bin(maxbins=30)),
                y='count()'
            ).properties(
                width=600,
                height=400,
                title=f"Distribution of {selected_column}"
            )
            st.altair_chart(histogram, use_container_width=True)
            
            
            top_20_values = get_top_20_frequent_values(col_data)
            st.write("Top 20 Most Frequent Values:")
            st.dataframe(top_20_values)
    else:
        st.warning("No numeric columns found in the dataset.")
