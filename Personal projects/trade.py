import robin_stocks.robinhood as rh
import pyotp
import schedule
import time
import pyodbc

# Set buy/sell amounts
Dollars = int(input("How much would you like your buys to be today: "))
Sell_price = float(input("What would you like the sell price to be today: "))

def trade_btc():
# Connect to SQL database
    cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'rh_orders')
    cursor = cnxn.cursor()

# login to robinhood
    totp = pyotp.TOTP("UZLHHA3Q2QXVZHNH").now()
    login = rh.login('dallinrima@gmail.com','Cougars123!', mfa_code = totp)

# find amount for buying and the amount in program
    with open('Personal projects/sell.txt', 'r') as s:
        Sell_price = float(s.read())

    with open('Personal projects/cash.txt', 'r') as c:
        programs_cash = float(c.read())

# Function to purchase BTC
    def Buy(Dollars):
        rh.order_buy_crypto_by_price('BTC', Dollars)

# Function to Sell BTC
    def Sell(sell_amount):
        rh.orders.order_sell_crypto_by_price('BTC', sell_amount)
    
# Finding BTC price
    BTC = float(rh.get_crypto_quote("BTC", info = 'mark_price'))

    print(f"Bitcoin price: {BTC}")
    print(f"Buy price: {Sell_price*.97}")

# Checking if BTC should be bought
    if BTC < (Sell_price * 0.97) and programs_cash > Dollars:
        Buy(Dollars)
        programs_cash = (programs_cash - Dollars)
        Sell_amount = (Dollars / .97)
        with open('Personal projects/cash.txt', 'w') as c:
            c.write(str(programs_cash))
        cursor.execute(f"Insert Into Orders (Order_Cost, Order_Amount, Bitcoin_Price, Sell_Price) Values ({Dollars}, {Sell_amount}, {BTC}, {Sell_price})")
        Sell_price = (Sell_price * 0.97)
        with open('Personal projects/sell.txt', 'w') as s:
            s.write(str(Sell_price))
        print('yes bought')

# Checking if BTC shoulde be sold
    Orders_sell_prices = []
    cursor.execute("select Sell_Price from Orders Order by Sell_Price")
    for row in cursor:
        Orders_sell_prices.append(row[0])
    print(Orders_sell_prices)

    for price in Orders_sell_prices:
        if BTC > price:
            cursor.execute(f"Select Order_Amount from Orders Where Sell_Price = {price}")
            for row in cursor:
                sell_amount = row[0]
                Sell(sell_amount)
                programs_cash = programs_cash + sell_amount
                with open('Personal projects/cash.txt', 'w') as c:
                    c.write(str(programs_cash))
                print('sold')
            cursor.execute(f"Delete from Orders where Sell_Price = {price}")
            Sell_price = (Sell_price / .97)
            with open('Personal projects/sell.txt', 'w') as s:
                s.write(str(Sell_price))

# Commits the actions taken in SQL database
    cnxn.commit() 

# Puts the program on repeating schedule, every 10 seconds
schedule.every(10).seconds.do(trade_btc)
while True:
    schedule.run_pending()
    time.sleep(1)
