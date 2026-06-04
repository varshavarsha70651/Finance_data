import streamlit as st
import pandas as pd
import plotly.express as px
from analysis import analyze_data
from utils import preprocess_data

st.set_page_config(page_title="Finance Analytics Dashboard", layout="wide")

st.title("📊 Finance Data Analytics Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data")
    st.dataframe(df.head())

    # Preprocess
    df = preprocess_data(df)

    # Analyze
    results = analyze_data(df)

    st.subheader("📈 Key Insights")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"{results['total_revenue']:.2f}")
    col2.metric("Total Expenses", f"{results['total_expense']:.2f}")
    col3.metric("Profit", f"{results['profit']:.2f}")

    st.subheader("📊 Visualizations")

    # Revenue over time
    if 'date' in df.columns:
        fig1 = px.line(df, x='date', y='revenue', title="Revenue Over Time")
        st.plotly_chart(fig1, use_container_width=True)

    # Expense distribution
    if 'category' in df.columns:
        fig2 = px.pie(df, names='category', values='expense', title="Expense Distribution")
        st.plotly_chart(fig2, use_container_width=True)

    # Correlation heatmap
    st.subheader("📌 Correlation Heatmap")
    fig3 = px.imshow(df.corr(numeric_only=True), text_auto=True)
    st.plotly_chart(fig3, use_container_width=True)

    st.success("✅ Analysis Complete!")
