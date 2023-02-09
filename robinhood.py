import robin_stocks.robinhood as rh
import pyotp
import pyodbc

# Connect to SQL database
cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'rh_orders')
cursor = cnxn.cursor()

# login to robinhood
totp = pyotp.TOTP("UZLHHA3Q2QXVZHNH").now()
login = rh.login('dallinrima@gmail.com','Cougars123!', mfa_code = totp)

class crypto:
    def __init__(self, ticker):
        self.ticker = ticker
        self.percent_change = float(input(f"What percent change would you like to base your purchases of {self.ticker} on? "))
        self.buy_dollars = float(input(f"How much would you like your buy amount of {self.ticker} to be? "))
        self.change_amount = (1 - (self.percent_change / 100))
        self.sell_dollars = (self.buy_dollars / self.change_amount)
        self.buy_price = float(input(f"At what price would you like to purchase {self.ticker}? "))
        self.sell_price = (self.buy_price / self.change_amount)
    
    def get_price(self):
        fails = 0
        try:
            self.current_price = float(rh.get_crypto_quote(self.ticker, info = 'mark_price'))
            return self.current_price
        except:
            print("Unable to get price")
            fails += 1
            self.get_price()
            if fails >= 10:
                quit()

    def buy_crypto(self):
        try:
            rh.order_buy_crypto_by_price(self.ticker, self.buy_dollars)
            cursor.execute(f"Insert Into buys (ticker, sell_price, sell_amount) Values ('{self.ticker}', {self.sell_price}, {self.sell_dollars})")
            self.buy_price = (self.buy_price * self.change_amount)
            self.sell_price = (self.sell_price * self.change_amount)
        except:
            print(f"Unable to purchase {self.ticker}")
            self.buy_crypto()

    def sell_crypto(self):
        try:
            rh.orders.order_sell_crypto_by_price(self.ticker, self.sell_dollars)
            self.buy_price = (self.buy_price / self.change_amount)
            self.sell_price = (self.sell_price / self.change_amount)
        except:
            print(f"Unable to sell {self.ticker}")
            self.sell_crypto()

def get_cryptos():
    crypto_tickers = []
    while True:
        crypto_ticker = input("What crypto currency would you like to trade today? Input a ticker or input q to move forward: ")
        if crypto_ticker != 'q':
            crypto_tickers.append(crypto_ticker)
        else:
            break
    return crypto_tickers

crypto_tickers = get_cryptos()
crypto_traders = []
for ticker in crypto_tickers:
    crypto_traders.append(crypto(ticker))

def trade_cryptos():
    for currency in crypto_traders:

        if currency.get_price() <= currency.buy_price:
            currency.buy_crypto()
        
        Orders_sell_prices = []
        cursor.execute(f"select sell_price from buys WHERE ticker = '{currency.ticker}' Order by sell_price")
        for row in cursor:
            Orders_sell_prices.append(row[0])
        for price in Orders_sell_prices:
            if currency.get_price() >= price:
                cursor.execute(f"Delete from buys where sell_price = {price}")
                currency.sell_crypto()

while True:
    trade_cryptos()
    cnxn.commit() 