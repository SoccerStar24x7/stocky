def retrieveData(stock):
    import yfinance as yf

    ticker = yf.Ticker(stock)

    data = ticker.history(period="1mo")
    data = data.drop(columns=["Dividends", "Stock Splits", "Capital Gains"])
    data = data.iloc(0)

    exportCSV(data)

def exportCSV(data):
    data.to_csv('data.csv', index=False)

if __name__ == "__main__":
    retrieveData("SPMO")
