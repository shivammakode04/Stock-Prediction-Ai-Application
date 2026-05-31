import yfinance as yf

def predict_price(symbol):
    data = yf.download(symbol, period="1y")
    last_price = data['Close'].iloc[-1]
    return {"symbol": symbol, "predicted_price": float(last_price) * 1.02}
