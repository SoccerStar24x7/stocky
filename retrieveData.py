def retrieveData(stock):
    import yfinance as yf

    ticker = yf.Ticker(stock)

    data = ticker.history(period="1mo")

    data = dataChange(data)

    exportCSV(data)

def exportCSV(data):
    data.to_csv('data.csv', index=False)

def dataChange(data):

    data = data.drop(columns=["Dividends", "Stock Splits", "Capital Gains"])
    data = data.drop(index=data.index[0])

    """
    for cell in data:
        print(cell)
        if (type(cell) == str):
            cell = ""
            continue
        cell = float(cell)
        cell *= 100
        cell = int(cell)
        cell /= 100
    """

    return data

if __name__ == "__main__":
    retrieveData("SPMO")

