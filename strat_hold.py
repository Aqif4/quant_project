import pandas as pd 
import sys  
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Import data
ticker= 'AAPL'

train_start="2000-01-01"
train_end="2020-01-01"

#This downloads the dataframe for the training period with adjusted prices
training_data=yf.download(ticker, start="2000-01-01", end= "2020-01-01", auto_adjust=True)

#This downloads the dataframe for the testing period with adjusted prices
testing_data=yf.download(ticker, start="2020-01-01", end= "2025-01-01", auto_adjust=True)

#Extract (adjusted) close data
training_closes=training_data['Close',str(ticker)]
testing_closes=testing_data['Close',str(ticker)]

#Calculate Sharpe ratio
def sharpe_calc(data):
    returns=np.array([])
    no_days=len(data)
    trading_days=252
    
    for i in np.arange(0,no_days-1):
        daily_return=(data.iloc[i+1]-data.iloc[i])/data.iloc[i]
        returns=np.append(returns,daily_return)
    
   
    mean_return=np.mean(returns)
    total_std_returns=np.std(returns)
    annual_std_returns=(total_std_returns*np.sqrt(trading_days/no_days))
    
    return mean_return/annual_std_returns

print(f'The Sharpe ratio from holding in the training data is {sharpe_calc(training_closes)}')
print(f'The Sharpe ratio from holding in the testing data is {sharpe_calc(testing_closes)}')

#Calculate max drawdown
def drawdown_calc(data):
    current_peak=data.iloc[0]
    drawdowns=np.array([])
    for close in data:
        if close < current_peak:
            current_drawdown=((close-current_peak)/current_peak)*100
            drawdowns=np.append(drawdowns,current_drawdown)
        else:
            current_peak=close
            drawdowns=np.append(drawdowns, 100)
    
    return np.min(drawdowns),np.argmin(drawdowns)

print(f'The max drawdown from holding in the training data is {drawdown_calc(training_closes)[0]}%')
print(f'The max drawdown from holding in the testing data is {drawdown_calc(testing_closes)[0]}%')