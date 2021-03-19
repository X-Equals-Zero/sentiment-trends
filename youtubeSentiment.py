from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import math

data = pd.read_csv('dated_titles.csv')
values = data['content'].values.tolist()
dates = data['date']
titles = data['title']
#values = pd.read_csv('titles.csv').values.tolist()

print(values)

sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]
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
