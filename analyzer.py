import os
from dotenv import load_dotenv

load_dotenv()

THRESHOLD = float(os.getenv("ALERT_THRESHOLD", 0.5))

def analyze_price(symbol, current_price, previous_close,news=None):
    change = current_price - previous_close
    change_percent = (change / previous_close) * 100
    
    print(f"Analyzing {symbol}...")
    print(f"Current: ${current_price:.2f} | Previous close: ${previous_close:.2f}")
    print(f"Change: ${change:.2f} ({change_percent:.2f}%)")
    
    if news:
        print(f"News context:")
        for headline in news[:3]:
            print(f"  - {headline}")

    if abs(change_percent) >= THRESHOLD:
        print(f"ALERT: {symbol} moved more than {THRESHOLD}% - worth flagging!")
        return True
    else:
        print(f"No significant movement.")
        return False