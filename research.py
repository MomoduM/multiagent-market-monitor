import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_stock_news(symbol):
    try:
        articles = newsapi.get_everything(
            q=symbol,
            language='en',
            sort_by='publishedAt',
            page_size=3
        )
        
        if not articles['articles']:
            return f"No recent news found for {symbol}"
        
        headlines = []
        for article in articles['articles']:
            headlines.append(article['title'])
        
        print(f"Found {len(headlines)} articles for {symbol}")
        return headlines
    
    except Exception as e:
        print(f"News fetch failed for {symbol}: {e}")
        return []

if __name__ == "__main__":
    results = get_stock_news("AAPL")
    for h in results:
        print(f"  - {h}")