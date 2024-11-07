import pandas as pd

def calculate_text_stats(col_data):
    """Calculate statistics for a text column."""
    num_unique = col_data.nunique()
    num_missing = col_data.isna().sum()
    num_empty = (col_data == "").sum()
    num_whitespace = (col_data.str.isspace()).sum()
    num_lowercase = (col_data.str.islower()).sum()
    num_uppercase = (col_data.str.isupper()).sum()
    num_alpha = (col_data.str.isalpha()).sum()
    num_numeric = (col_data.str.isnumeric()).sum()
    mode_value = col_data.mode().iloc[0] if not col_data.mode().empty else "N/A"
    
    stats_data = {
        "Metric": [
            "Number of Unique Values", "Number of Missing Values", "Empty Strings",
            "Whitespace Only", "Lowercase Only", "Uppercase Only", "Alphabetic Only",
            "Numeric Only", "Mode Value"
        ],
        "Value": [
            num_unique, num_missing, num_empty, num_whitespace, 
            num_lowercase, num_uppercase, num_alpha, num_numeric, mode_value
        ]
    }
    return pd.DataFrame(stats_data)

def get_top_20_frequent_values(col_data):
    """Get top 20 most frequent values with their percentages."""
    top_20_values = col_data.value_counts().head(20).reset_index()
    top_20_values.columns = ["Value", "Occurrences"]
    total_count = len(col_data)
    top_20_values["Percentage"] = (top_20_values["Occurrences"] / total_count * 100).round(2)
    return top_20_values
