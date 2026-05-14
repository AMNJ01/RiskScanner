import yfinance as yf
import pandas as pd

def analyze_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        
        if df.empty:
            return None, "Ticker not found."

        current_price = df['Close'].iloc[-1]
        high_52w = df['High'].max()
        drop_percent = ((high_52w - current_price) / high_52w) * 100
        
        ma_50 = df['Close'].rolling(window=50).mean().iloc[-1]
        
        risk_score = 0
        reasons = []

        if drop_percent > 15:
            risk_score += 40
            reasons.append(f"High Drawdown: {drop_percent:.1f}% off 52W high.")
        
        if current_price < ma_50:
            risk_score += 30
            reasons.append("Trading below 50-day Moving Average.")

        recent_vol = df['Close'].pct_change().tail(10).std() * 100
        if recent_vol > 2.5:
            risk_score += 30
            reasons.append("High recent volatility detected.")

        risk_score = min(risk_score, 100)
        conclusion = "RISKY" if risk_score >= 50 else "STABLE"

        chart_df = df.tail(30)
        chart_data = {
            "dates": chart_df.index.strftime('%d %b').tolist(),
            "prices": [round(p, 2) for p in chart_df['Close'].tolist()]
        }

        return {
            "price": round(current_price, 2),
            "high_52w": round(high_52w, 2),
            "drop_percent": round(drop_percent, 2),
            "risk_score": risk_score,
            "conclusion": conclusion,
            "reasons": reasons,
            "chart": chart_data
        }, None
    except Exception as e:
        return None, str(e)