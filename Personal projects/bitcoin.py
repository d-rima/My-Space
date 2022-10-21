import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.google.com/search?q=value+of+bitcoin&oq=value+of+bitcoin&aqs=chrome..69i57.3776j0j1&sourceid=chrome&ie=UTF-8'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, "html.parser")

    identification = soup.find(id="crypto-updatable_2")

    price = identification.find("span", class_="pclqee").get_text()
    price_value = float(price.replace(',',''))

    print(price_value)

    if price_value < 28000:
        send_mail()

# Writing a program to send and Email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
    subject = 'Price Fell Down!'
    body = 'Buy Bitcoin Now!'
    msg = f"Subject: {subject}\n\n{body} "
    server.sendmail(
        'dallinrima@gmail.com',
        'dallinrima@gmail.com',
        msg
    )
    
    server.quit()

check_price()