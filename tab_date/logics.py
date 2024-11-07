

import pandas as pd
from datetime import datetime

def calculate_date_stats(col_data):
    """Calculate statistics for a date column."""
    num_unique = col_data.nunique()
    num_missing = col_data.isna().sum()
    min_date = col_data.min()
    max_date = col_data.max()
    weekend_days = col_data[col_data.dt.weekday >= 5].count()
    weekday_days = col_data[col_data.dt.weekday < 5].count()
    future_dates = col_data[col_data > datetime.now()].count()
    occurrences_1900 = (col_data == "1900-01-01").sum()
    occurrences_1970 = (col_data == "1970-01-01").sum()
    
    stats_data = {
        "Metric": [
            "Number of Unique Values", "Number of Missing Values", "Minimum Date",
            "Maximum Date", "Weekend Days", "Weekday Days", 
            "Future Dates", "Occurrences of 1900-01-01", "Occurrences of 1970-01-01"
        ],
        "Value": [
            num_unique, num_missing, min_date, max_date, weekend_days, 
            weekday_days, future_dates, occurrences_1900, occurrences_1970
        ]
    }
    return pd.DataFrame(stats_data)

def get_top_20_frequent_dates(col_data):
    """Get top 20 most frequent dates with their percentages."""
    top_20_dates = col_data.value_counts().head(20).reset_index()
    top_20_dates.columns = ["Date", "Occurrences"]
    total_count = len(col_data)
    top_20_dates["Percentage"] = (top_20_dates["Occurrences"] / total_count * 100).round(2)
    return top_20_dates
