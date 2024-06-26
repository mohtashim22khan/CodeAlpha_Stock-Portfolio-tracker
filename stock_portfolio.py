import yfinance as yf
import pandas as pd
class StockPortfolio:
    def __init__(self):
        self.portfolio={}
    def add_stock(self,symbol,shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]["Shares"]+=shares
        else:
            self.portfolio[symbol]={"Shares":shares}
    def remove_stock(self,symbol,shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol]["Shares"]>shares:
                self.portfolio[symbol]["Shares"]-=shares
            else:
                del self.portfolio[symbol]
    def track_performance(self):
        Total_value=0
        for symbol,data in self.portfolio.items():
            try:
                stock=yf.Ticker(symbol)
                history=stock.history(period="1d")
                if not history.empty:
                    current_price=history["Close"].iloc[0]
                    value=current_price*data["Shares"]
                    print(f"{symbol}:Shares-{data['Shares']},Current Price-{current_price},value-{value}")
                    Total_value+=value
                else:
                    print(f"Error, No data avalaible for {symbol}, it may be delisted")
            except ValueError:
                print(f"failed to retrieve data for {symbol} ")
        print(f"Total portfolio value:{Total_value}")
portfolio=StockPortfolio()
while True:
    print("\n1. Add stock")
    print("2. Remove stock")
    print("3. track performance")
    print("4. Exit")        
    choice=input("Enter your choice")
    if choice=="1":
        symbol=input("Enter stock symbol:").upper()
        shares=int(input("Enetr number of shares"))
        portfolio.add_stock(symbol,shares)
        print("Stock added to portfolio")
    elif choice=="2":
        symbol=input("Enter stock symbol to remove").upper()
        shares=int(input("enter no of shares to remove"))
        portfolio.remove_stock(symbol,shares)
        print("Stock removed from portfolio")
    elif choice=="3":
        portfolio.track_performance()
    elif choice=="4":
        print("Thanks for Using,Have a nice day")
        break
    else:
        print("Invalid choice")
        
