# загружать данные можно из (Quandl, Intrinion, AlphaVantage, Tiingo, IEX Cloud, etc.)
# https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt

plt.interactive(True)

tsla_df = yf.download(['TSLA'], start='2021-08-20', end='2021-08-21', progress=False, interval="1m")
print(tsla_df.head())

ticker = yf.Ticker('TSLA')
tsla_df = ticker.history(period="max")
tsla_df['Close'].plot(title="TSLA's stock price")

print(ticker.major_holders)
print(ticker.institutional_holders)
