# 🚀 RiskScanner
**Advanced Technical Sentiment & Risk Engine**

RiskScanner is a high-performance web dashboard designed to help traders identify the risk level of any stock in real-time. By analyzing price action, trend strength, and volatility, it provides a clear "Stable" vs "Risky" verdict.

## 🎯 Project Moto
"Empowering traders with data-driven risk intelligence to avoid falling knives."

## 🛠️ Tech Stack
- **Backend:** Python (Flask, yfinance, Pandas)
- **Frontend:** HTML5, CSS3 (Electric Sky Theme), JavaScript (ES6)
- **Visualization:** Chart.js

## 📊 Core Features
- **Proprietary Risk Scoring:** A 0-100% score based on 52-week drawdown and 50-day moving averages.
- **Dynamic UI:** The dashboard automatically switches to a "Danger Theme" when a stock is high-risk.
- **NSE Support:** Native support for Indian stocks using the `.NS` suffix logic.
- **Interactive Charts:** Real-time 30-day price trend visualization.

## 🚀 Local Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/RiskScanner.git](https://github.com/YOUR_USERNAME/RiskScanner.git)

2. Navigate to the backend folder:

Bash
cd backend

3. Install dependencies:

Bash
pip install -r requirements.txt

4. Run the application:
   ```bash
   python app.py
   
5. Open your browser and go to http://127.0.0.1:5000

👨‍💻 Author
Amandeep Jana

Electronics and Communication Engineering Student, VIT Bhopal University


---

### 3. The `requirements.txt` File
In your `backend` folder, make sure this file exists with these exact lines:
```text
flask
flask-cors
yfinance
pandas
gunicorn   