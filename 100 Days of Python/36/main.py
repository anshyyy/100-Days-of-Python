from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "OJ582O3DG8W2ZH74"
news_key = "a22fd2762b5c455dafed390d0549f02f"
sid = "AC12a7c7332b2e85ed30413ade5535ddd3"
token = "f0006ca6eb38f7eeac70d4258d887ae1"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "apikey": api_key,
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA"
}
parameters1 = {
    "apiKey": news_key,
    "q": COMPANY_NAME,
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_cp = yesterday["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_cp = day_before_yesterday["4. close"]

difference = float(yesterday_cp) - float(day_before_yesterday_cp)
increase = False
if difference >= 0:
    increase = True

if increase:
    per_diff = (abs(difference) / float(day_before_yesterday_cp)) * 100
    response1 = requests.get(url=NEWS_ENDPOINT, params=parameters1)
    news = response1.json()["articles"]
    articles = news[:3]
    headlines = [f"Headline :{article['title']}.\nBrief: {article['description']}" for article in articles]
    print(headlines)
    client = Client(sid, token)
    for article in headlines:
        message = client.messages.create(
            body=article,
            from_="+19842063537",
            to="+917903553605"
        )
        print(message.sid)


else:
    print("Decrease by:")
    per_diff = (abs(difference) / float(yesterday_cp)) * 100

print(round(per_diff))
