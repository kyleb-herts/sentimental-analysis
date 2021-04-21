#this code uses examples from https://nealcaren.org/lessons/wordlists/

import pandas as pd
from afinn import Afinn
import matplotlib.pyplot as plt
from datetime import datetime

afinn = Afinn(language='en', emoticons=True)

pd.set_option('display.max_rows', None)

data = pd.read_csv("reviews_pseudoanonymised.csv")
data['afinn_score'] = data['comment'].apply(afinn.score)

#Sets up blank y_co_ords array
y_co_ords=[]
#Iterates over data in panda array and adds it to python array
for i in data['afinn_score']:
  y_co_ords.append(i)

#Sorts the elements of the data into order
y_co_ords.sort()

#Sets minimum value as -14 (as this was established from previous analysis)
val=-14.0
#Array to be appended to depending on the frequency of each value
scores=[]
#Ready to store the x values of each score
x_values=[]

#Iterates 59 times due to range of scores that were established in previous analysis
for i in range(59):
  #Adds the frequency of a score to the scores array
  scores.append(y_co_ords.count(val))
  #Adds the x value that is to be corresponding to that score
  x_values.append(val)
  #Increments the val by 1 every iteration
  val=val+1

#Plots the frequency for the relevant scores
plt.scatter(x_values, scores)
#Labels the axes frequency and Score value
plt.xlabel('Score value', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
#Displays the graph on the screen
plt.show()
