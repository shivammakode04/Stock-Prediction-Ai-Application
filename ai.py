import requests, os

def get_stock_news(symbol):
    key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={key}"
    return requests.get(url).json().get("articles", [])[:5]
