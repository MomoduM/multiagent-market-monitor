import os
from dotenv import load_dotenv

from fetcher import fetch_price
from analyzer import analyze_price
from notifier import send_alert

load_dotenv()

SYMBOL = os.getenv("SYMBOL")

# Agent 1 — Fetch the data
data = fetch_price(SYMBOL)

if data is None:
    print("Could not fetch data - rate limit or API error. Try again in a minute.")
else:
    # Agent 2 — Analyze it
    alert_triggered = analyze_price(
        data["symbol"],
        data["price"],
        data["previous_close"]
    )
    
    # Agent 3 — Notify if alert was triggered
    if alert_triggered:
        send_alert(
            data["symbol"],
            data["price"],
            data["change_percent"]
        )
    else:
        print("No alert needed - market movement within normal range.")