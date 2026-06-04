import streamlit as st
import pandas as pd
import plotly.express as px
from analysis import basic_info, clean_data, calculate_kpis, time_series, group_by_category

st.set_page_config(page_title="Finance Analyzer", layout="wide")

st.title("📊 Finance Data Analyzer")

# Upload CSV
file = st.file_uploader("Upload your finance CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    df = clean_data(df)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # KPIs
    st.subheader("📊 KPIs")
    kpis = calculate_kpis(df)

    cols = st.columns(len(kpis))
    for i, (key, value) in enumerate(kpis.items()):
        cols[i].metric(key, f"{value:,.2f}")

    # Basic Stats
    st.subheader("📈 Statistical Summary")
    st.dataframe(basic_info(df))

    # Time Series Plot
    st.subheader("📉 Trend Analysis")
    ts_df, date_col = time_series(df)

    if ts_df is not None:
        num_cols = ts_df.select_dtypes(include='number').columns
        selected_col = st.selectbox("Select metric", num_cols)

        fig = px.line(ts_df, x=date_col, y=selected_col, title="Trend")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No date column found for time analysis")

    # Category Analysis
    st.subheader("📊 Category Analysis")

    grouped = group_by_category(df)
    if grouped is not None:
        st.dataframe(grouped)

        col = st.selectbox("Select column for bar chart", grouped.columns)
        fig = px.bar(grouped, y=col, title="Category Comparison")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No category column found")

else:
    st.info("👆 Upload a CSV file to start analysis")
