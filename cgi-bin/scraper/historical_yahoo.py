import fix_yahoo_finance as yf
import datetime

all_data = {}
start = datetime.datetime(2018,4,10)
end = datetime.datetime(2018,5,10)

for ticker in ['AAPL', 'GOOG', '0005.HK']:
    all_data[ticker] = yf.download(ticker, start = start, end = end)
    # cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    # all_data[ticker].reindex(columns=cols)


print (all_data['GOOG'])


# column : "Open" | "High" | "Low" | "Close" | "Adj Close" | "Volume"
# column = 'Close'
# list = all_data['GOOG'][column].tolist()
#
# print list
#
# index = all_data['GOOG'].index.tolist()
#
# print index
