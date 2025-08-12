import numpy as np
from scipy.stats import norm
import yfinance as yf
from datetime import date

# Define the Black-Scholes formula for a European call option
def black_scholes_call_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    return price

# --- 1. GATHERING THE INPUTS ---
TICKER = '^NSEI'
STRIKE_PRICE = 24000.0
EXPIRATION_DATE = date(2025, 8, 28)
TODAY = date.today()

# --- 2. GETTING LIVE DATA & CALCULATING PARAMETERS ---
nifty_data = yf.Ticker(TICKER)
SPOT_PRICE = nifty_data.history(period='1d')['Close'].iloc[0]
T = (EXPIRATION_DATE - TODAY).days / 365.0
RISK_FREE_RATE = 0.07 # 7%
hist_data = nifty_data.history(period='1y')
log_returns = np.log(hist_data['Close'] / hist_data['Close'].shift(1))
VOLATILITY = log_returns.std() * np.sqrt(252)

# --- 3. CALCULATE THE OPTION PRICE ---
theoretical_price = black_scholes_call_price(SPOT_PRICE, STRIKE_PRICE, T, RISK_FREE_RATE, VOLATILITY)

# --- 4. DISPLAY THE RESULTS ---
print("--- NIFTY 50 Option Pricing Analysis ---")
print(f"Date: {TODAY}")
print(f"Current NIFTY 50 Price (S): {SPOT_PRICE:.2f}")
print(f"Strike Price (K): {STRIKE_PRICE:.2f}")
print(f"Days to Expiration: {(EXPIRATION_DATE - TODAY).days}")
print(f"Risk-Free Rate (r): {RISK_FREE_RATE:.2%}")
print(f"Annualized Volatility (sigma): {VOLATILITY:.2%}")
print("------------------------------------------")
print(f"Theoretical Call Option Price: ₹ {theoretical_price:.2f}")