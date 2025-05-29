# 🚀 Crypto ETL Dashboard

This is an end-to-end ETL (Extract, Transform, Load) project that collects live cryptocurrency data using the CoinGecko API, stores it in a SQLite database, processes it with Python, and visualizes the data with Matplotlib.

---

## 📌 Features

- 🔄 Automated daily ETL pipeline using Windows Task Scheduler
- 📡 Live crypto price extraction from CoinGecko API (Bitcoin, Ethereum, Dogecoin)
- 🧹 Cleaned and transformed data stored in `crypto_clean.csv`
- 💾 SQLite database (`crypto.db`) for persistence
- 📊 Visualization in Jupyter Notebook using `matplotlib`

---

## 🛠️ Tech Stack

| Component    | Tool              |
|--------------|-------------------|
| Language     | Python            |
| ETL Script   | `etl.py`          |
| Visualization | Jupyter Notebook |
| Database     | SQLite            |
| API Source   | CoinGecko         |
| Automation   | Windows Task Scheduler |

---

## 🗂️ Folder Structure

![Crypto ETL Architecture](crypto_etl_architecture.png)


