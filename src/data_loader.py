# src/data_loader.py

import yfinance as yf
import pandas as pd

def download_price_data(tickers, start='2015-01-01', end='2024-12-31'):
    """
    Download adjusted close price data using yfinance.

    Parameters:
    - tickers (list): List of ticker symbols (e.g., ['TCS.NS', 'RELIANCE.NS'])
    - start (str): Start date (format: YYYY-MM-DD)
    - end (str): End date (format: YYYY-MM-DD)

    Returns:
    - DataFrame: Adjusted close prices of the selected tickers
    """
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data
