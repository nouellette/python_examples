import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def plot_data(stock_data, sma_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Stock Price')
    for window, sma in sma_data.items():
        plt.plot(sma, label=f'SMA {window} Days')
    plt.title('Stock Prices with Simple Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    stock_data = yf.download('AAPL', start=datetime(2023, 1, 1), end=datetime.now())
    print(stock_data.head())

    sma_windows = [20, 50, 100]
    sma_data = {window: stock_data['Close'].rolling(window=window).mean() for window in sma_windows}

    plot_data(stock_data, sma_data)

if __name__ == '__main__':
    main()