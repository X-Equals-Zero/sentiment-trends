import pandas as pd
import matplotlib
import json
import ast

data = pd.read_csv('labeled.csv')

scores = data['rating'].values.tolist()

df = pd.DataFrame()

print(scores[0])
for score in scores:
    broken = ast.literal_eval(score)
    tmp = pd.DataFrame.from_records([broken])
    # use ignore_index for appending df's or else it will keep appending index 0's
    df = df.append(tmp, ignore_index=True) 

df2 = pd.DataFrame()
df2['neg'] = df['neg']
df2['neu'] = df['neu']
df2['pos'] = df['pos']
df2['compound'] = df['compound']
df2['date'] = data['date']
df2['title'] = data['title']
print(df2.head())
df2.to_csv('final.csv', index=False)
#print(data['date'])
