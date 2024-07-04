import pandas as pd
import numpy as np

stock = pd.read_csv('./store_1_stock.csv')
print(f"Total quantity: {stock['Quantity'].sum()}")
print(f"Max quantity: {stock['Quantity'].max()}")