

import pandas as pd

def get_summary_info(df):
    """Get summary information of the DataFrame."""
    num_rows = df.shape[0]
    num_columns = df.shape[1]
    num_duplicates = df.duplicated().sum()
    num_missing = df.isnull().any(axis=1).sum()
    
    summary_data = {
        "Metric": ["Number of Rows", "Number of Columns", "No of Duplicated Rows", "No of Rows with Missing Values"],
        "Value": [num_rows, num_columns, num_duplicates, num_missing]
    }
    return pd.DataFrame(summary_data)

def get_column_info(df):
    """Get column information including name, data type, and memory usage."""
    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Memory Usage (KB)": (df.memory_usage(deep=True)[1:] / 1024).round(2)  # Exclude index memory usage
    })
    column_info['Data Type'] = column_info['Data Type'].replace({
        'object': 'Text', 
        'int64': 'Numeric', 
        'float64': 'Numeric', 
        'datetime64[ns]': 'Date'
    })
    return column_info
