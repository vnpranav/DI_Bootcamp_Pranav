import pandas as pd
import numpy as np

stock = pd.read_csv('./store_1_stock.csv')
stock.set_index('Unnamed: 0')

stock['Sale-price'] = stock['Price-per-kg'] * 0.9
stock.drop(['Color'], axis=1, inplace=True)
stock.rename(columns={'Price-per-kg' : 'Price'}, inplace=True)


new_fruits = pd.DataFrame({
   'Quantity' : np.nan,
   'Price' : 3.5,
   'Sale-price' : 3.15,
}, index=['Grape'])

df = pd.concat([stock, new_fruits], ignore_index=True)
print(df)