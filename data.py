import yfinance as yf
import pandas as pd
import requests


def get_stock_data(symbol, period="1y"):

    try:
        ticker = symbol + ".NS"

        df = yf.download(ticker, period=period)

        if df.empty:
            return pd.DataFrame()

        df = df.reset_index()

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.dropna()

        
        df["Daily_Return"] = (df["Close"] - df["Open"]) / df["Open"]

        df["MA7"] = df["Close"].rolling(7).mean()

        if "Date" in df.columns:
            df["Date"] = df["Date"].astype(str)

        df = df.fillna(0)

        return df

    except Exception:
        return pd.DataFrame()


def get_market_news():

    API_KEY = "0ca7a9f0e5b14bab96780b906816bc64"

    url = f"https://newsapi.org/v2/everything?q=stock%20market&language=en&sortBy=publishedAt&apiKey={API_KEY}"

    try:

        response = requests.get(url)

        data = response.json()

        articles = data["articles"][:5]

        news = []

        for article in articles:

            news.append({
                "title": article["title"],
                "url": article["url"],
                "source": article["source"]["name"]
            })

        return news

    except Exception:
        return []