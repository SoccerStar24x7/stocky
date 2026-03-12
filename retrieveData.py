from yahoo_fin as yfin
ticker = "SPMO"

data = yfin.stock_info.get_quote_table(ticker, False)

print(data)