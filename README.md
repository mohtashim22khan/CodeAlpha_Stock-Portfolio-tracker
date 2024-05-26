1. Import Statements
 yfinance: A Python library used to access stock data from Yahoo Finance.
pandas: A powerful data manipulation and analysis library in Python. Though imported, it's not used directly in this script.
2.StockPortfolio Class
The StockPortfolio class contains methods to manage the stock portfolio
Initializes an empty dictionary portfolio to store the stock symbols and the number of shares
*add_stock Method:
Adds stocks to the portfolio.
If the stock symbol already exists, it increases the number of shares.
If the stock symbol does not exist, it adds a new entry with the symbol and shares.
remove_stock Method
*Removes stocks from the portfolio.
If the stock symbol exists and the number of shares to remove is less than the current shares, it decreases the number of shares.
If the shares to remove are equal to or greater than the current shares, it removes the stock entry from the portfolio
*Track_performance Method
Tracks the performance of the portfolio by calculating the total value.
For each stock in the portfolio:
Retrieves the stock's historical data for the last day using yfinance.
Checks if the data is available.
Retrieves the closing price of the stock.
Calculates the total value of shares for that stock.
Prints the stock's details and value.
Adds the value to the total portfolio value.
Prints the total portfolio value at the end.
3.Main Loop
Creates an instance of StockPortfolio.
Provides a menu-driven interface to interact with the portfolio:
Option 1: Add stock to the portfolio.
Option 2: Remove stock from the portfolio.
Option 3: Track the performance of the portfolio.
Option 4: Exit the program.
Takes user input to perform the desired action.
Ensures the program continues running until the user chooses to exit.
SUMMARY:
Initialization: An empty portfolio dictionary.
Add Stock: Add or update the number of shares for a stock symbol.
Remove Stock: Reduce or delete the number of shares for a stock symbol.
Track Performance: Retrieve the latest stock prices and calculate the total portfolio value.
User Interaction: A menu-driven loop that allows users to add, remove, track, or exit.
