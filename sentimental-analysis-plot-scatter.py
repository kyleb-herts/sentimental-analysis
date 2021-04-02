
#!/usr/bin/python

#this code uses examples from https://nealcaren.org/lessons/wordlists/

import pandas as pd
from afinn import Afinn
import matplotlib.pyplot as plt

afinn = Afinn(language='en', emoticons=True)

pd.set_option('display.max_rows', None)

data = pd.read_csv("reviews_pseudoanonymised.csv")
data['afinn_score'] = data['comment'].apply(afinn.score)

d = {"comment":data['afinn_score'].index.tolist(), "score":data['afinn_score'].array}
df = pd.DataFrame(data=d)
df.plot.scatter(x="comment", y="score")
plt.show()
# df = pd.DataFrame({"x":keys, "score":values})
# ax = df.plot.scatter(x='x', y='score')
# plt.show()




# columns_to_display = ['comment', 'afinn_score']
# filtered_data = data.sort_values(by='afinn_score', ascending=False)[columns_to_display]

#print("\n")
#print(filtered_data)
#print("\n")
#print("Afinn Score From Comments Summary")
#print(data['afinn_score'].describe())

# filtered_data.to_csv('reviews_pseudoanonymised_afinn_score_applied.csv')
# data['afinn_score'].describe().to_csv('afinn_score_summary.csv')
# print("Sentiment Analyis completed - AFINN score applied")
