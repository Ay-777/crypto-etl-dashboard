import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/processed/crypto_clean.csv")

st.title("📊 Crypto Dashboard with Filters")
st.markdown("Visualize current crypto metrics interactively.")

# Sidebar Filters
crypto_options = df["id"].unique().tolist()
selected_cryptos = st.sidebar.multiselect("Select Cryptocurrencies", crypto_options, default=crypto_options)

chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Log Scale Bar"])

# Filter Data
filtered_df = df[df["id"].isin(selected_cryptos)]

# Display filtered table (optional)
with st.expander("🔍 View Filtered Data"):
    st.dataframe(filtered_df)

# Plot
st.subheader(f"{chart_type} for Selected Cryptos")

fig, ax = plt.subplots()

if chart_type == "Bar Chart":
    ax.bar(filtered_df["id"], filtered_df["current_price"], color="skyblue")
    ax.set_ylabel("Price (USD)")
    ax.set_title("Current Prices")

elif chart_type == "Line Chart":
    ax.plot(filtered_df["id"], filtered_df["current_price"], marker="o", linestyle='-')
    ax.set_ylabel("Price (USD)")
    ax.set_title("Price Trend")

elif chart_type == "Log Scale Bar":
    ax.bar(filtered_df["id"], filtered_df["current_price"], color="salmon")
    ax.set_yscale("log")
    ax.set_ylabel("Price (Log Scale)")
    ax.set_title("Current Prices (Log Scale)")

ax.set_xlabel("Cryptocurrency")
plt.xticks(rotation=45)
st.pyplot(fig)
