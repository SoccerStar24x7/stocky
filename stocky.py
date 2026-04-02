import plotext as plt
def retrieveData(stock, start = "1/01/2026", end = plt.today_datetime()):

    import yfinance as yf
    import plotext as plt

    plt.date_form('d/m/Y')
    start = plt.string_to_datetime(start)

    data = yf.download(stock, start, end, progress = False)

    return data


def show(data, stock):
    import plotext as plt
    import pandas as pd
    
    # Flatten MultiIndex columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    dates = plt.datetimes_to_string(data.index)

    # Pass OHLC data explicitly as a dictionary
    ohlc = {
        'Open':  data['Open'].tolist(),
        'High':  data['High'].tolist(),
        'Low':   data['Low'].tolist(),
        'Close': data['Close'].tolist(),
    }

    plt.candlestick(dates, ohlc)
    plt.title(f"{stock} Stock Price")
    plt.xlabel("Date")
    # plt.ylabel("Stock Price $")

    plt.theme('pro')
    plt.plotsize(100, 30)

    plt.show()

def main():

    import argparse as ap
    import plotext as plt

    parser = ap.ArgumentParser(description="A tool that enables you to see stocks, straight from your terminal.")

    # 2. Add arguments (the "..." in your prompt)
    # A positional argument (required)
    parser.add_argument('ticker', default = "SPMO", help='The stock ticker symbol (e.g., AAPL)')
    
    # An optional argument (flag)
    parser.add_argument('--start', default='1/01/2026', help='Starting date (d/m/y)')

    time = plt.today_datetime()

    parser.add_argument('--end', default=time, help='Ending date (d/m/y)')

    # 3. Parse the arguments
    args = parser.parse_args()

    stock = args.ticker.upper()
    start = args.start
    end = args.end

    if end != time:
        end = plt.string_to_datetime(end)

    data = retrieveData(stock, start = start, end = end)

    show(data, stock)


if __name__ == "__main__":
    main()
