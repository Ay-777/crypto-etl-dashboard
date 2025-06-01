import requests
import pandas as pd
import sqlite3
from datetime import datetime
import os
import logging
from notification import send_email


# Set up logging
logging.basicConfig(
    filename='etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1. Extract
def extract():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": "bitcoin,ethereum,dogecoin",
            "order": "market_cap_desc"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)

        # Add extraction timestamp
        df["extracted_at"] = datetime.utcnow()

        # Append to CSV or create new one
        file_exists = os.path.isfile('crypto_data.csv')
        if not file_exists:
            logging.info("🆕 'crypto_data.csv' not found — creating a new file.")
        df.to_csv('crypto_data.csv', mode='a', header=not file_exists, index=False)

        # Save raw file
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/crypto_raw.csv", index=False)

        logging.info("✅ Data extracted and saved successfully.")
        return df

    except Exception as e:
        logging.error(f"❌ Extraction failed: {e}")
        raise

# 2. Transform
def transform(df):
    try:
        df = df[[
            "id", "symbol", "current_price", "market_cap",
            "total_volume", "last_updated", "extracted_at"
        ]]
        df["last_updated"] = pd.to_datetime(df["last_updated"])

        os.makedirs("data/processed", exist_ok=True)
        df.to_csv("data/processed/crypto_clean.csv", index=False)

        logging.info("✅ Data transformed and cleaned.")
        return df

    except Exception as e:
        logging.error(f"❌ Transformation failed: {e}")
        raise

# 3. Load
def load(df):
    try:
        conn = sqlite3.connect("crypto.db")
        df.to_sql("crypto_prices", conn, if_exists="append", index=False)
        conn.close()

        logging.info("✅ Data loaded into SQLite database.")
    except Exception as e:
        logging.error(f"❌ Loading failed: {e}")
        raise

# Run the ETL
if __name__ == "__main__":
    try:
        raw_df = extract()
        clean_df = transform(raw_df)
        load(clean_df)
        print("✅ ETL pipeline completed.")
    except Exception as err:
        print("❌ ETL pipeline failed. Check etl.log for details.")
        error_message = f"ETL pipeline failed: {err}"
        logging.error(error_message)
        send_email("❌ ETL Pipeline Failed", error_message)
