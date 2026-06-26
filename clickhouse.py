# ClickHouse setup and data storage functions

import os
import clickhouse_connect
from dotenv import load_dotenv

load_dotenv()

client = clickhouse_connect.get_client(
    host=os.getenv("URL_CLICKHOUSE"),
    username=os.getenv("USER_CLICKHOUSE"),
    password=os.getenv("PASSWORD_CLICKHOUSE"),
    secure=True
)

def query_stock(symbol):
    result = client.query(f"""
        SELECT symbol, price, change_percent, timestamp 
        FROM stock_prices 
        WHERE symbol = '{symbol}'
        ORDER BY timestamp DESC 
        LIMIT 10
    """)
    return result.result_rows


def setup_table():
    client.command('''
        CREATE TABLE IF NOT EXISTS stock_prices (
            symbol String,
            price Float64,
            previous_close Float64,
            change Float64,
            change_percent String,
            timestamp DateTime DEFAULT now()
        ) ENGINE = MergeTree()
        ORDER BY (symbol, timestamp)
    ''')
    print("ClickHouse table ready")



def store_price(data):
    client.insert('stock_prices', [[
        data['symbol'],
        data['price'],
        data['previous_close'],
        data['change'],
        data['change_percent']
    ]], column_names=['symbol','price','previous_close','change','change_percent'])
    print(f"Stored {data['symbol']} price in ClickHouse")

if __name__ == "__main__":
    setup_table()