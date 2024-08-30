import requests
import datetime as dt
from twilio.rest import Client

STOCK = "IBM"
COMPANY_NAME = "IBM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TS_LIST_DAILY = "Time Series (Daily)"
CLOSE_PRICE = "4. close"

ARTICLES = "articles"

TODAY_DATE = dt.datetime.today()

news_api = ""
stocks_api = "demo"
account_sid = ""
auth_token = ""

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api,
}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stocks_api,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

stocks_response = requests.get(STOCK_ENDPOINT, stock_parameters)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()
tesla_stocks_time_series_data = stocks_data[TS_LIST_DAILY]

yesterday_date = str((TODAY_DATE - dt.timedelta(1)).date())
day_before_yesterday_date = str((TODAY_DATE - dt.timedelta(2)).date())

yesterday_stock_close_price = float(tesla_stocks_time_series_data[yesterday_date][CLOSE_PRICE])
day_before_yesterday_stock_close_price = float(tesla_stocks_time_series_data[day_before_yesterday_date][CLOSE_PRICE])

difference_in_stock_price_percent = round(((yesterday_stock_close_price - day_before_yesterday_stock_close_price)
                                           / yesterday_stock_close_price) * 100)

if (yesterday_stock_close_price - day_before_yesterday_stock_close_price) < 0:
    stock = f"{STOCK}: 🔻{difference_in_stock_price_percent}%"
else:
    stock = f"{STOCK}: 🔺{difference_in_stock_price_percent}%"

if abs(difference_in_stock_price_percent) >= 0:
    top_3_news = news_data[ARTICLES][2:5]
    top_3_title_description = [(article["title"], article["description"]) for article in top_3_news]
    for item in top_3_title_description:
        content = f"{stock}\nHeadline: {item[0]}\nBrief: {item[1]}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{content}",
            from_="",
            to="",
        )
