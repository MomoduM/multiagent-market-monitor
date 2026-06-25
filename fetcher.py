import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
SYMBOL = os.getenv("SYMBOL")

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

fetch_price(SYMBOL)