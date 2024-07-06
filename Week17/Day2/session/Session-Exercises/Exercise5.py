import pandas as pd

stock = pd.read_csv('./store_1_stock.csv')


print(stock.loc[2, 'Quantity'])
