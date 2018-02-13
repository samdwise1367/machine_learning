import pandas as pd
import quandl

#df = quandl.get('WIKI/PRICES')
#data = quandl.get_table('WIKI/PRICES')
#print(data.head())


df = quandl.get('NSE/OIL')

df = df[['Open','High','Low','Close']]
df['HL_PCT'] = (df['Open'] - df['Close']) / df['Close'] * 100.0

df = df[['Open','Close','HL_PCT']]

print(df.head())