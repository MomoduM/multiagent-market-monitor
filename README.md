# Multiagent Market Monitor

A three-agent system that monitors stock prices in real time and sends SMS alerts when significant price movements are detected.

## Agents
- **Fetcher** — pulls live stock prices via Alpha Vantage API
- **Analyzer** — detects significant price movements against a configurable threshold
- **Notifier** — sends SMS alerts via Twilio when thresholds are breached

## Tech Stack
Python, Alpha Vantage API, Twilio, python-dotenv

## Setup
1. Clone the repo
2. Create a `.env` file with your API keys (see `.env.example`)
3. Install dependencies: `pip install requests twilio python-dotenv`
4. Run: `python3 main.py`