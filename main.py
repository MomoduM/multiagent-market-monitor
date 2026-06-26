import os
from dotenv import load_dotenv
from clickhouse import setup_table
from fetcher import run_fetcher

load_dotenv()

if __name__ == "__main__":
    setup_table()
    run_fetcher()