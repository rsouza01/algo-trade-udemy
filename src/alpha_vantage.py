# importing libraries

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time
import os

key_path = "D:\\Udemy\\Quantitative Investing Using Python\\1_Getting Data\\AlphaVantage\\key.txt"

# extracting data for a single ticker
ts = TimeSeries(key=os.environ['ALPHA_API_KEY'], output_format='pandas')
data = ts.get_daily(symbol='EURUSD', outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]
data = data.iloc[::-1]


# extracting stock data (historical close price) for multiple stocks
all_tickers = ["AMZN","GOOG"]
close_prices = pd.DataFrame()
api_call_count = 1
ts = TimeSeries(key=os.environ['ALPHA_API_KEY'], output_format='pandas')
start_time = time.time()
for ticker in all_tickers:
    print("Retrieving " + ticker)
    data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='compact')[0]
    api_call_count+=1
    data.columns = ["open","high","low","close","volume"]
    data = data.iloc[::-1]
    close_prices[ticker] = data["close"]
    if api_call_count==5:
        api_call_count = 1
        time.sleep(60 - ((time.time() - start_time) % 60.0))
    print(data)
    print("Done.")


# # extracting ohlcv data for multiple stocks
# all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG",
#                "FB","BA","MMM","XOM","NKE","INTC"]
# ohlv_dict = {}
# api_call_count = 1
# ts = TimeSeries(key=os.environ['ALPHA_API_KEY'], output_format='pandas')
# start_time = time.time()
# for ticker in all_tickers:
#     data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='compact')[0]
#     api_call_count+=1
#     data.columns = ["open","high","low","close","volume"]
#     data = data.iloc[::-1]
#     ohlv_dict[ticker] = data
#     if api_call_count==5:
#         api_call_count = 1
#         time.sleep(60 - ((time.time() - start_time) % 60.0))