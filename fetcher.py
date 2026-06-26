import os
import requests
import time
from clickhouse import store_price
from analyzer import analyze_price
from notifier import send_alert
from dotenv import load_dotenv
from research import get_stock_news

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
SYMBOL = os.getenv("SYMBOL").split(",")  # Support multiple symbols

def fetch_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "Global Quote" not in data or not data["Global Quote"]:
        print(f"API error or rate limit hit: {data}")
        return None

    quote = data["Global Quote"]
    
    result = {
        "symbol": quote["01. symbol"],
        "price": float(quote["05. price"]),
        "previous_close": float(quote["08. previous close"]),
        "change": float(quote["09. change"]),
        "change_percent": quote["10. change percent"]
    }

    print(f"Fetched {symbol}: ${result['price']}")
    return result

def run_fetcher():
    while True:
        for symbol in SYMBOL:
            result = fetch_price(symbol)
            if result:
                store_price(result)

                        # Research agent - get news context
                news = get_stock_news(symbol)
                result['news'] = news

                alert_triggered = analyze_price(result["symbol"], result["price"], result["previous_close"], result.get('news'))
                if alert_triggered:
                    try:
                        send_alert(result["symbol"], result["price"], result["change_percent"])
                    except Exception as e:
                        print(f"Error sending alert for {result['symbol']}: {e}")
                    time.sleep(15)  # avoid rate limit between stocks
        print("Waiting 5 minutes...")
        time.sleep(300)

if __name__ == "__main__":
    run_fetcher() # Run the fetcher in a loop to continuously fetch data every 5 minutes



