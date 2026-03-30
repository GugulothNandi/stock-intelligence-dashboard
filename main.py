from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data import get_stock_data, get_market_news

app = FastAPI(
    title="Stock Data Intelligence API",
    description="Mini Financial Data Platform for Internship Assignment",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

companies = [
    "TCS",
    "INFY",
    "RELIANCE",
    "HDFCBANK",
    "ICICIBANK",
    "WIPRO",
    "LT"
]


@app.get("/")
def home():
    return {"message": "Welcome to Stock Intelligence Dashboard API"}


@app.get("/companies")
def get_companies():
    return {"companies": companies}


@app.get("/data/{symbol}")
def get_data(symbol: str):

    df = get_stock_data(symbol, "30d")

    if df.empty:
        return {"error": "No data found"}

    return df.to_dict(orient="records")


@app.get("/summary/{symbol}")
def summary(symbol: str):

    df = get_stock_data(symbol, "1y")

    if df.empty:
        return {"error": "No data found"}

    return {
        "symbol": symbol,
        "52_week_high": float(df["Close"].max()),
        "52_week_low": float(df["Close"].min()),
        "average_close": float(df["Close"].mean())
    }


@app.get("/compare")
def compare(symbol1: str, symbol2: str):

    df1 = get_stock_data(symbol1, "30d")
    df2 = get_stock_data(symbol2, "30d")

    if df1.empty or df2.empty:
        return {"error": "Invalid symbols"}

    perf1 = df1["Close"].pct_change().sum()
    perf2 = df2["Close"].pct_change().sum()

    return {
        symbol1: float(perf1),
        symbol2: float(perf2)
    }


@app.get("/volatility/{symbol}")
def volatility(symbol: str):

    df = get_stock_data(symbol, "1y")

    if df.empty:
        return {"error": "No data"}

    volatility_score = df["Close"].pct_change().std()

    return {
        "symbol": symbol,
        "volatility_score": float(volatility_score)
    }


@app.get("/momentum/{symbol}")
def momentum(symbol: str):

    df = get_stock_data(symbol, "90d")

    if df.empty:
        return {"error": "No data"}

    momentum_value = df["Close"].iloc[-1] - df["Close"].iloc[-7]

    trend = "Bullish" if momentum_value > 0 else "Bearish"

    return {
        "symbol": symbol,
        "momentum": float(momentum_value),
        "trend": trend
    }


@app.get("/correlation")
def correlation(symbol1: str, symbol2: str):

    df1 = get_stock_data(symbol1, "1y")
    df2 = get_stock_data(symbol2, "1y")

    if df1.empty or df2.empty:
        return {"error": "Invalid symbols"}

    corr = df1["Close"].corr(df2["Close"])

    return {
        "symbol1": symbol1,
        "symbol2": symbol2,
        "correlation": float(corr)
    }


@app.get("/top-movers")
def top_movers():

    results = []

    for company in companies:

        df = get_stock_data(company, "5d")

        if df.empty:
            continue

        change = df["Close"].pct_change().sum()

        results.append({
            "symbol": company,
            "change": float(change)
        })

    results = sorted(results, key=lambda x: x["change"], reverse=True)

    return {
        "top_gainers": results[:3],
        "top_losers": results[-3:]
    }


@app.get("/news")
def market_news():

    news = get_market_news()

    return {"news": news}