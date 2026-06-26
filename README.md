# Multiagent Market Monitor

An autonomous multi-agent system that monitors stock prices in real time, stores historical data in ClickHouse, enriches alerts with live news context, and sends SMS notifications when significant price movements are detected.

Built at the Tessl AI Multiagent Hackathon, London 2026.

## Architecture
main.py

└── Fetcher Agent          → pulls live prices via Alpha Vantage every 5 mins

└── ClickHouse Agent → stores all price data to ClickHouse Cloud

└── Research Agent   → fetches live news headlines per stock

└── Analyzer Agent   → detects price movements above threshold

└── Notifier Agent → sends SMS alert via Twilio

## Agents

- **Fetcher** — polls Alpha Vantage every 5 minutes for a configurable watchlist of stocks
- **ClickHouse** — logs every price fetch to ClickHouse Cloud for historical querying
- **Research** — fetches 3 latest news headlines per stock via NewsAPI for context
- **Analyzer** — compares current price vs previous close, triggers alert if movement exceeds threshold
- **Notifier** — sends SMS alert via Twilio with symbol, price, and % change

## Sponsor Tools Used

| Tool | Usage |
|------|-------|
| Alpha Vantage | Live stock price data |
| ClickHouse Cloud | Historical price storage and querying |
| Twilio | SMS alert notifications |
| NewsAPI | Real-time news context per stock |

## Demo

```bash
# Run the full pipeline
python main.py

# Query historical prices for a stock
python query.py
```

## Setup

1. Clone the repo
2. Create virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install requests twilio python-dotenv clickhouse-connect newsapi-python`
4. Copy `.env.example` to `.env` and fill in your API keys
5. Run: `python main.py`

## Environment Variables
ALPHA_VANTAGE_KEY=your-key

SYMBOL=AAPL,MSFT,GOOGL

ALERT_THRESHOLD=0.5

TWILIO_ACCOUNT_SID=your-sid

TWILIO_AUTH_TOKEN=your-token

TWILIO_NUMBER=your-twilio-number

YOUR_NUMBER=your-phone-number

URL_CLICKHOUSE=your-host

USER_CLICKHOUSE=default

PASSWORD_CLICKHOUSE=your-password

NEWS_API_KEY=your-key

## Tech Stack

Python · Alpha Vantage · ClickHouse Cloud · Twilio · NewsAPI