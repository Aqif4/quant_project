import pandas as pd 
import sys  
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#Import data
ticker= sys.argv[1]

start="2000-01-01"
end="2020-01-01"

#This downloads the dataframe with adjusted prices
data=yf.download(ticker, start=start, end= end, auto_adjust=True)

#Extract (adjusted) close data
closes=data['Close',str(ticker)]

#Compare the price on the previous day to the price of the previous x day moving average
def x_day_mean_reversion(x):
    x_mean_reversion_days=0
    for i in np.arange(x,len(closes)):
        x_day_period=np.array(closes.iloc[i-x:i])
        average=np.mean(x_day_period)
        #Price goes up if below the mean
        if closes.iloc[i-1] < average and closes.iloc[i]>closes.iloc[i-1]:
            x_mean_reversion_days+=1
        #Price goes down if above the mean
        elif closes.iloc[i-1] > average and closes.iloc[i] < closes.iloc[i-1]:
            x_mean_reversion_days+=1
    return 100*(x_mean_reversion_days/len(np.arange(x,len(closes))))

#Find the best x day period
array=np.array([])

for period in range(1,101):
    array=np.append(array, x_day_mean_reversion(period))

accuracy=array.max()
best_period=array.argmax()+1

#Graph of best period for interest
plt.plot(range(1,101),array)
plt.xlabel("Period")
plt.ylabel("Accuracy")
#plt.show()

print(f'The accuracy of the best mean reversion for {ticker} is {accuracy}% with a period of {best_period} days')


