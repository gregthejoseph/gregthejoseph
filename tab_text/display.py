
import streamlit as st
import altair as alt
from tab_text.logics import calculate_text_stats, get_top_20_frequent_values

def display_text_series_analysis(df):
    """Display the text series analysis in Streamlit."""
    st.header("Text Series Analysis")
    
    text_columns = df.select_dtypes(include=['object']).columns.tolist()
    if text_columns:

        selected_column = st.selectbox("Select a text column for analysis:", text_columns)
        
        if selected_column:
            col_data = df[selected_column]
            
            
            stats_df = calculate_text_stats(col_data)
            st.table(stats_df)
            
           
            value_counts = col_data.value_counts().reset_index()
            value_counts.columns = [selected_column, "Occurrences"]
            
            bar_chart = alt.Chart(value_counts).mark_bar().encode(
                x=alt.X(selected_column, sort="-y"),
                y="Occurrences"
            ).properties(
                width=600,
                height=400,
                title=f"Occurrences of Values in {selected_column}"
            )
            st.altair_chart(bar_chart, use_container_width=True)
            
            
            top_20 = get_top_20_frequent_values(col_data)
            st.write("Top 20 Most Frequent Values:")
            st.dataframe(top_20)
    else:
        st.warning("No text columns found in the dataset.")
