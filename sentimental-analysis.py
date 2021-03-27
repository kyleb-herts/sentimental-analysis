
#!/usr/bin/python

#this code uses examples from https://nealcaren.org/lessons/wordlists/

import pandas as pd
from afinn import Afinn

afinn = Afinn(language='en')

pd.set_option('display.max_rows', None)

data = pd.read_csv("reviews_pseudoanonymised.csv")
data['afinn_score'] = data['comment'].apply(afinn.score)

columns_to_display = ['comment', 'afinn_score']
filtered_data = data.sort_values(by='afinn_score')[columns_to_display]

print("\n")
print(data.sort_values(by='afinn_score')[columns_to_display])
print("\n")
print("Afinn Score From Comments Summary")
print(data['afinn_score'].describe())

filtered_data.to_csv('reviews_pseudoanonymised_afinn_score_applied.csv')
data['afinn_score'].describe().to_csv('afinn_score_summary.csv')
