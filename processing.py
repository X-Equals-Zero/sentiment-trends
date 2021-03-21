import pandas as pd
import matplotlib

#joins the title and description 
#df = pd.read_csv('query.csv')
df = pd.read_csv('query.csv', parse_dates=['snippet.publishTime'])

df['date'] = pd.to_datetime(df['snippet.publishTime'])
df = df.sort_values(by='date')

df['empty'] = ' ' 
df2 = pd.DataFrame()

df2['content'] = df['snippet.title'] + df['empty'] + df['snippet.description']
df2['title'] = df['snippet.title']

df2['date'] = df['snippet.publishTime']
print(df2.head())
df2.to_csv('dated_titles.csv', index=False)

