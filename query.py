from clickhouse import query_stock

def main():
    print("=== Market Monitor - Stock Query ===")
    symbol = input("Enter stock symbol to query (e.g. AAPL): ").upper()
    results = query_stock(symbol)

    if results:
        print(f"\nLast 10 prices for {symbol}:")
        print("-" * 50)
        for row in results:
            print(f"  Time: {row[3]} | Price: ${row[1]:.2f} | Change: {row[2]}")
    else:
        print(f"No data found for {symbol} — make sure main.py has fetched it first")

if __name__ == "__main__":
    main()