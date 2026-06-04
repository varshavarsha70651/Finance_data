import pandas as pd

def basic_info(df):
    return df.describe()

def clean_data(df):
    # Try converting date column automatically
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors='ignore')
    return df

def calculate_kpis(df):
    numeric_cols = df.select_dtypes(include='number').columns

    kpis = {}
    for col in numeric_cols:
        kpis[f"Total {col}"] = df[col].sum()

    return kpis

def time_series(df):
    for col in df.columns:
        if "date" in col.lower():
            df = df.sort_values(col)
            return df, col
    return None, None

def group_by_category(df):
    cat_cols = df.select_dtypes(include='object').columns
    num_cols = df.select_dtypes(include='number').columns

    if len(cat_cols) > 0:
        return df.groupby(cat_cols[0])[num_cols].sum()
    return None
