NIFTY 50 Option Pricer
This project contains a Python script to calculate the theoretical price of a NIFTY 50 European call option using the Black-Scholes model. It fetches live market data for the NIFTY 50 index and calculates its historical volatility to provide a real-time theoretical valuation.

Features
Black-Scholes Model: Implements the standard formula for European call options.

Live Data: Fetches the current spot price of the NIFTY 50 index from Yahoo Finance.

Historical Volatility: Automatically calculates the annualized historical volatility based on the last year of NIFTY 50 data.

Configurable: Easily change the strike price and expiration date directly in the script to analyze different options.

Requirements
All required Python libraries are listed in the requirements.txt file.

Python 3.x

numpy

scipy

yfinance

Setup
Clone the repository or download the files.

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies:

pip install -r requirements.txt

How to Run the Script
Configure the option parameters inside the option_pricer.py script. You can set the STRIKE_PRICE and EXPIRATION_DATE to match the option you want to analyze.

# Example configuration
STRIKE_PRICE = 24000.0
EXPIRATION_DATE = date(2025, 8, 28)

Execute the script from your terminal:

python option_pricer.py

The script will output the analysis, including all the model inputs and the final theoretical option price.

--- NIFTY 50 Option Pricing Analysis ---
Date: 2024-08-13
Current NIFTY 50 Price (S): 24420.50
Strike Price (K): 24000.00
Days to Expiration: 380
Risk-Free Rate (r): 7.00%
Annualized Volatility (sigma): 14.50%
------------------------------------------
Theoretical Call Option Price: ₹ 2245.78
