import pandas as pd

stock = pd.read_csv('./store_1_stock.csv')
print(stock.head(1))
print(stock.tail(1))
print(stock.describe())

print(stock['Quantity'].sum())
print(stock.nlargest(2,'Price-per-kg'))