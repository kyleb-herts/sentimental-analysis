
#!/usr/bin/python

#this code uses examples from https://nealcaren.org/lessons/wordlists/

import pandas as pd
from afinn import Afinn
import matplotlib.pyplot as plt
from datetime import datetime


def get_month(text_string):
    date = datetime.strptime(text_string, '%d/%m/%Y')
    return date.month


afinn = Afinn(language='en', emoticons=True)

pd.set_option('display.max_rows', None)

data = pd.read_csv("reviews_pseudoanonymised.csv")
data['month'] = data['date'].apply(get_month)
data['afinn_score'] = data['comment'].apply(afinn.score)

d = {"month":data['month'].array, "score":data['afinn_score'].array}
df = pd.DataFrame(data=d)
dk = df.groupby('month').sum()
dk.plot.bar()
plt.show()
