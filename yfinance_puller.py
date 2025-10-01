import yfinance as yf
import sys

ticker= sys.argv[1]

start="2024-01-01"
end="2025-01-01"

data=yf.download(ticker, start=start, end= end)

data.to_csv(f"./raw_data/{ticker}_prices_from_{start}_to_{end}.csv")

