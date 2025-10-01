import pandas as pd 
import sys  
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Import data
ticker= sys.argv[1]

start="2000-01-01"
end="2025-01-01"

#This downloads the dataframe with adjusted prices
data=yf.download(ticker, start=start, end= end, auto_adjust=True)

#Extract (adjusted) close data
closes=data['Close',str(ticker)]

#Compare the price on a day to the price on the previous day
momentum_days=0

for i in np.arange(1,len(closes)):
    if closes.iloc[i] > closes.iloc[i-1]:
        momentum_days+=1

print(f"The accuracy of 1-day momentum is {100*(momentum_days/(len(closes)-1))}% for {ticker}")

