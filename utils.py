import pandas as pd

def preprocess_data(df):
    # Convert date column if exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Fill missing values
    df.fillna(0, inplace=True)

    return df
