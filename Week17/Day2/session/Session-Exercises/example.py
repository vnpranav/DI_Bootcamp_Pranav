import pandas as pd
pd.options.mode.copy_on_write = True #prevent warning
df = pd.read_csv('./second_hand_cars.csv') #gets all rows
# print(df.head(5))

shortened = df[['Company Name', 'Car Name', 'Variant', 'Price', 'Make Year']] #filter/slice  dataset
# print(shortened.head(5))
shortened.drop(['Make Year'], inplace=True, axis=1)
print('First 5 cars')
print(shortened.head(5))

# access specific location : df.loc, df.iloc : iloc does not accept boolean data/ conditions
# print(f"Mean Price of first 5 cars: {shortened['Price'][0:5].mean()}")

# increment all prices
shortened = shortened[['Price']] + 50000
print(f"Mean Price of first 5 cars: {shortened['Price'][0:5].mean()}")

# count missing values
# print(df.isna().sum())

# dropping null values
corrected = df.dropna(inplace=True) #or use inplace = True

df.fillna(0, inplace=True) #can do it for specific columns as well
# print(df.isna().sum())

# change data type
df['Price'] = df['Price'].astype('Float64')
# print(df['Price'])

# convert column to series
prices = pd.Series(df['Price'])
companies = pd.Series(df['Company Name'])

# # mapping in series
# print(df['Company Name'].unique())
# df['Company Name'] = df['Company Name'].map({'Ford': 'Fart'})

# # get unique
# print(df['Company Name'].unique())

# grouping
print(df.groupby('Company Name').count())