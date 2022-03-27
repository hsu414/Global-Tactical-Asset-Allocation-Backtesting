
import datetime
import yfinance as yf 

tickers = ['TSM','TSLA']
start = datetime.datetime.now() - datetime.timedelta(days=180)
end = datetime.date.today()

# stock_dr = yf.download(tickers,start,end)
# print(stock_dr)
print(yf.download(tickers, period='1mo')['Adj Close'])