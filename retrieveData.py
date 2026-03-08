from yahoo_fin.stock_info import *
ticker = "SPMO"

data = get_quote_table(ticker, False)

print(data)