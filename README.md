# 📊 Stock Intelligence Dashboard

A **real-time stock data analytics platform** built using **FastAPI**, **Python**, and **Chart.js**.  
Track stock prices, visualize trends, calculate volatility & momentum, and read the latest market news — all in one interactive dashboard.

---

## 🚀 Features

- **Stock Data & Analysis**
  - Last 30 days stock prices
  - 7-day moving averages
  - Daily returns

- **Financial Metrics**
  - 52-week high & low
  - Average closing price
  - Volatility score
  - Momentum trend (Bullish/Bearish)

- **Market Overview**
  - Top gainers and losers among tracked companies
  - Stock correlation analysis

- **News Feed**
  - Latest market news pulled from an API

- **Interactive Dashboard**
  - Beautiful, dark-themed dashboard
  - Line chart visualization with Chart.js
  - Responsive design for web browsers

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, Chart.js
- **Data:** yFinance API, News API
- **Environment Management:** `.env` for API keys
- **Dependencies:** See `requirements.txt`

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/GugulothNandi/stock-intelligence-dashboard.git
cd stock-intelligence-dashboard

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Create a .env file in the root directory:
NEWS_API_KEY=your_news_api_key_here
Run the FastAPI server:
uvicorn main:app --reload
Open the dashboard:

Open frontend/index.html in your browser.

Note: Make sure FastAPI server is running at http://127.0.0.1:8000
