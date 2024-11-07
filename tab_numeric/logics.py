
import pandas as pd

def calculate_numeric_stats(col_data):
    """Calculate statistics for a numeric column."""
    num_unique = col_data.nunique()
    num_missing = col_data.isna().sum()
    num_zeros = (col_data == 0).sum()
    num_negatives = (col_data < 0).sum()
    avg_value = col_data.mean()
    std_dev = col_data.std()
    min_value = col_data.min()
    max_value = col_data.max()
    median_value = col_data.median()
    
    stats_data = {
        "Metric": [
            "Number of Unique Values", "Number of Missing Values", "Occurrences of 0",
            "Negative Values", "Average Value", "Standard Deviation", 
            "Minimum Value", "Maximum Value", "Median Value"
        ],
        "Value": [
            num_unique, num_missing, num_zeros, num_negatives, avg_value, 
            std_dev, min_value, max_value, median_value
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
