def analyze_data(df):
    results = {}

    if 'revenue' in df.columns:
        results['total_revenue'] = df['revenue'].sum()
    else:
        results['total_revenue'] = 0

    if 'expense' in df.columns:
        results['total_expense'] = df['expense'].sum()
    else:
        results['total_expense'] = 0

    results['profit'] = results['total_revenue'] - results['total_expense']

    return results
