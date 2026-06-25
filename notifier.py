import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
YOUR_NUMBER = os.getenv("YOUR_NUMBER")

def send_alert(symbol, price, change_percent):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    message = client.messages.create(
        body=f"MARKET ALERT: {symbol} is at ${price:.2f} ({change_percent} change) — threshold breached!",
        from_=TWILIO_NUMBER,
        to=YOUR_NUMBER
    )
    
    print(f"Alert sent! Message SID: {message.sid}")
    return message.sid