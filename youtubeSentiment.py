from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import math

data = pd.read_csv('dated_titles.csv')
values = data['content'].values.tolist()
dates = data['date']
titles = data['title']
#values = pd.read_csv('titles.csv').values.tolist()


print(values)
analyzer = SentimentIntensityAnalyzer()
ratings = []
for sentence in values:
    #for sentence in item:
    #if(sentence == sentence):
        vs = analyzer.polarity_scores(str(sentence))
        print("{:-<65} {}".format(sentence, str(vs)))
        print(str(vs))
        temp = [vs]
        ratings.append(vs)

final = pd.DataFrame()
final['rating'] = ratings
final['date'] = dates
final['title'] = titles
print(final)
final.to_csv('labeled.csv', index=False)
