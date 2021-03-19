import requests
import pandas as pd
import json
import sys

QUERY = 'crypto'
KEY = 'AIzaSyBrffDBZkxpPnf71efJeHvYpfXwDX2F1r4'
if len(sys.argv) > 1:
    QUERY = sys.argv[1]



url ='https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + QUERY + '&key='+ KEY + '&maxResults=50'

print(url)
print(url)
print(url)
x = requests.get(url, headers={'User-Agent': 'Custom'}).json()
df = pd.DataFrame(pd.json_normalize(x['items']))
print(df.head())
df.to_csv('query.csv', index=False)
