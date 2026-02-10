import streamlit as st
import pandas as pd

st.title("Data Analysis")

# Load dataset
df = pd.read_csv("Dataset/Sales Clenad_df.csv")

# Sales by Product Category
st.subheader("Sales by Product Category")
st.write("This analysis identifies which product categories generate the highest total revenue.")

category_sales = (
    df.groupby("item type")["total revenue"]
      .sum()
      .sort_values(ascending=False)
)

st.bar_chart(category_sales)

st.caption("A small number of product categories contribute the majority of total revenue.")

# Average Order Value by Region
st.subheader("Average Order Value by Region")
st.write("Average Order Value (AOV) is calculated as total revenue divided by number of orders.")

aov = (
    df.groupby("region")
      .agg(
          revenue=("total revenue", "sum"),
          orders=("order id", "nunique")
      )
)

aov["AOV"] = aov["revenue"] / aov["orders"]
aov = aov.sort_values("AOV", ascending=False)

st.bar_chart(aov["AOV"])

st.caption("Average order value is relatively consistent across regions, with minor variation.")
