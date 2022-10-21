import requests
import smtplib
import datetime

date = datetime.datetime.now()
year = date.year
month = str(date.month)
day = str(date.day)

if len(day) < 2:
    day = f'0{day}'
if len(month) < 2:
    month = f"0{month}"


today = f"{year}-{month}-{day}"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
price_api_key = "96740ZKHS5QKU8N7"
news_api_key = "cb6ad4ead48242ef862499020794be73"

func = 'TIME_SERIES_DAILY'
symbol = STOCK
OWM_ENDPOINT = "https://www.alphavantage.co/query?"

stock_paramaters = {
    "function": func,
    "symbol": symbol,
    "apikey": price_api_key
}

response = requests.get(OWM_ENDPOINT, params = stock_paramaters)
data = response.json()["Time Series (Daily)"][today]

open = float(data["1. open"])
close = float(data["4. close"])

def send_mail(text, articles):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
    subject = 'Tesla Price Shift!'
    body = f'{text}{articles}'
    msg = f"Subject: {subject}\n\n{body} "
    server.sendmail(
        'dallinrima@gmail.com',
        "dallinrima@gmail.com",
        msg
    )
    
    server.quit()

def get_news():
    article_list = []
    OWM_ENDPOINT2 = "https://newsapi.org/v2/everything?"
    news_api_key = "cb6ad4ead48242ef862499020794be73"
    COMPANY_NAME = "Tesla Inc"
    search_params = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
        "from": today,
        "language": "en",
        "pageSize": 3
    }
    response = requests.get(OWM_ENDPOINT2, params = search_params)
    data = response.json()["articles"]
    for article in data:
        article_list.append(article["url"])
    articles = f'1. {article_list[0]}\n2. {article_list[1]}\n3. {article_list[2]}'
    send_mail(text, articles)


if open < close:
    math = open/close
    percent = (math % 1) * -100
    text = f"Tesla climbed {percent}%!\nThis could be why:\n"

if open > close:
    math = close/open
    percent = 100 - ((math % 1) * 100)
    text = f"Tesla dropped {percent}%!\nThis could be why:\n"

if abs(percent) >= 5:
    get_news()



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

