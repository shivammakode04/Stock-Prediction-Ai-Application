from fastapi import FastAPI
from model import predict_price
from news import get_stock_news
from ai import get_ai_insights, analyze_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/predict/{symbol}")
def predict(symbol: str):
    return predict_price(symbol)

@app.get("/news/{symbol}")
def news(symbol: str):
    return {"news": get_stock_news(symbol)}

@app.get("/insights/{symbol}")
def insights(symbol: str):
    return get_ai_insights(symbol)

@app.get("/sentiment/{symbol}")
def sentiment(symbol: str):
    return analyze_sentiment(symbol)
