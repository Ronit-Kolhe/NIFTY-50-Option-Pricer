# 📈 NIFTY 50 Option Pricer

A Python-based tool to calculate the **theoretical price of a NIFTY 50 European Call Option** using the **Black-Scholes Model**. The script fetches **live NIFTY 50 market data** and calculates **historical volatility** to provide a real-time theoretical valuation.

## ✨ Features
- **Black-Scholes Model**: Implements the standard formula for European call options.
- **Live Market Data**: Fetches the latest NIFTY 50 spot price from Yahoo Finance.
- **Historical Volatility**: Calculates annualized historical volatility from the past year of data.
- **Customizable**: Easily update strike price and expiration date directly in the script.
- **Real-Time Analysis**: Get the most recent option price with a single run.

## 📦 Requirements
- Python 3.x  
- Dependencies (listed in `requirements.txt`):
  - numpy
  - scipy
  - yfinance

## ⚙️ Setup
```bash
git clone https://github.com/yourusername/nifty50-option-pricer.git
cd nifty50-option-pricer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

🚀 How to Run

1. Open option_pricer.py and set your parameters:



STRIKE_PRICE = 24000.0
EXPIRATION_DATE = date(2025, 8, 28)

2. Run the script:



python option_pricer.py

📊 Example Output

--- NIFTY 50 Option Pricing Analysis ---
Date: 2024-08-13
Current NIFTY 50 Price (S): 24420.50
Strike Price (K): 24000.00
Days to Expiration: 380
Risk-Free Rate (r): 7.00%
Annualized Volatility (sigma): 14.50%
Theoretical Call Option Price: ₹ 2245.78