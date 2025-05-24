import requests
import pandas as pd
import sqlite3
from datetime import datetime

# 1. Extract
def extract():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": "bitcoin,ethereum,dogecoin", "order": "market_cap_desc"}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("data/raw/crypto_raw.csv", index=False)
    return df

# 2. Transform
def transform(df):
    df = df[["id", "symbol", "current_price", "market_cap", "total_volume", "last_updated"]]
    df["last_updated"] = pd.to_datetime(df["last_updated"])
    df["extracted_at"] = datetime.utcnow()
    df.to_csv("data/processed/crypto_clean.csv", index=False)
    return df

# 3. Load
def load(df):
    conn = sqlite3.connect("crypto.db")
    df.to_sql("crypto_prices", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    raw_df = extract()
    clean_df = transform(raw_df)
    load(clean_df)
    print("ETL pipeline completed.")
