import pandas as pd
import numpy as np

stock = pd.read_csv('./store_1_stock.csv')
print(stock['Quantity'].dtype)