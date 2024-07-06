import pandas as pd
df = pd.read_csv('./second_hand_cars.csv')

df2 = df[df['Make Year'] > 2015] #filter
print(df2['Make Year'].unique())

# use queries
df3 = df.query("`Make Year` > 2015 and `Price` > 300000")
print(df3['Make Year'].min(axis=None))
print(df3['Price'].min(axis=None))

df4 = df3.groupby('Company Name').count()
df4.plot(kind='pie', subplots=True)
# to check error
