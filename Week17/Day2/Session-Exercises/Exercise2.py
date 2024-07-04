import pandas as pd
sales_df = pd.DataFrame({
   'Quantity' : [20, 30, 15, 10],
   'Color' : ['Red', 'Yellow', 'Red', 'Brown'],
   'Price-per-kg' : [3,2,4,5]
}, index=['Apples', 'Bananas', 'Cherries', 'Dates'])

# store dataframe in csv file
sales_df.to_csv('store_1_stock.csv')