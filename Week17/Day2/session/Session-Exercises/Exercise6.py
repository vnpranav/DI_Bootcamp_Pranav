import pandas as pd

stock = pd.read_csv('./store_1_stock.csv')
stock.set_index('Unnamed: 0')

stock['Sale-price'] = stock['Price-per-kg'] * 0.9
stock.drop(['Color'], axis=1)
stock.rename(columns={'Price-per-kg' : 'Price'}, inplace=True)

print(stock)