import requests
import pandas as pd
import json
import sys

QUERY = 'crypto'
KEYFILE = open('.key.txt', 'r')
KEY = KEYFILE.read()
KEYFILE.close()
print(KEY)
MAXRES = '50'
NEXTPAGE = ''

if len(sys.argv) > 1:
    QUERY = sys.argv[1]

def nextPage(page):
    

    print("TRIGGERED ===============================")
    print(str(len(page)))
    if len(page) > 1:
        
        return('&pageToken=' + page)
    else:
        return('')

def url():
    temp = 'https://www.googleapis.com/youtube/v3/search?part=snippet' + nextPage(NEXTPAGE) + '&q=' + QUERY + '&key='+ KEY + '&maxResults=' + MAXRES
    return(temp)

x = requests.get(url(), headers={'user-agent': 'custom'}).json()
NEXTPAGE = x['nextPageToken']

print(NEXTPAGE + "<-- NEXT page url")
x1 = requests.get(url(), headers={'user-agent': 'custom'}).json()
print(url())

df = pd.DataFrame(pd.json_normalize(x['items']))
df = df.append(pd.DataFrame(pd.json_normalize(x1['items'])))
print(df.head())

df.to_csv('query.csv', index=False)
