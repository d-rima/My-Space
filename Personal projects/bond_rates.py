import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}

def get_short_bonds(headers):
    URL1 = 'https://ycharts.com/indicators/2_year_treasury_rate#:~:text=2%20Year%20Treasury%20Rate%20is%20at%203.40%25%2C%20compared%20to%203.06,long%20term%20average%20of%203.14%25.'

    page1 = requests.get(URL1, headers = headers)

    soup1 = BeautifulSoup(page1.content, "html.parser")

    short_bonds = soup1.find("div", class_=("key-stat-title")).get_text().strip()
    short_bonds_numerical = float(short_bonds[0:4])

    print(f'Short term bond yields: {short_bonds_numerical}')
    return(short_bonds_numerical)

def get_long_bond(headers):
    URL2 = 'https://ycharts.com/indicators/10_year_treasury_rate'

    page2 = requests.get(URL2, headers = headers)

    soup2 = BeautifulSoup(page2.content, "html.parser")

    long_bonds = soup2.find("div", class_="key-stat-title").get_text().strip()
    long_bonds_numerical = float(long_bonds[0:4])

    print(f'Long term bond yields: {long_bonds_numerical}')
    return long_bonds_numerical

short_bond = get_short_bonds(headers)
long_bond = get_long_bond(headers)

indicator = (long_bond - short_bond)

print(f'The difference between long and short term bond yields is: {indicator}')
if indicator > 0:
    print('Recession indicator has not been met')
else:
    print('Recession indicator has been met')