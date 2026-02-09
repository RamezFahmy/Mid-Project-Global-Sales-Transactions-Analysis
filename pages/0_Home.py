import streamlit as st
import pandas as pd

st.title("Home")
st.header("Global Sales Transactions Analysis")

st.write("""
This application presents a mid-project analysis of global sales transactions
across regions, product categories, and sales channels.
""")

df = pd.read_csv("Dataset/Sales Cleaned_df.csv")

st.subheader("Dataset Overview")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")
st.dataframe(df.head())
