
#!/usr/bin/python

#this code uses examples from https://nealcaren.org/lessons/wordlists/

#import pandas an open source data analysis and manipulation tool - https://pandas.pydata.org/
import pandas as pd

#import afinn to  utilise afinn wordlist for sentimental analysis - https://github.com/fnielsen/afinn
from afinn import Afinn

def modify_helpful_value(text_string):
    # NaN value reurn 1.0
    if text_string != text_string:
        return 1.0
    else:
        return text_string

#set afinn language to English and enable afinn score of emoticons
afinn = Afinn(language='en', emoticons=True)

#in pandas set option to display all table rows
pd.set_option('display.max_rows', None)

#read data from provided csv file
data = pd.read_csv("reviews_pseudoanonymised.csv")

# Add the helpful column as the factor of the overall score
# if helpful column is nothing, return 1; otherwise, return original value
data['helpful'] = data['helpful'].apply(modify_helpful_value)

#apply afinn score to comments
data['afinn_score'] = data['comment'].apply(afinn.score)

#set column output to only be the comment and afinn score
columns_to_display = ['comment', 'afinn_score']

#set rows to be sorted by afinn score
filtered_data = data.sort_values(by='afinn_score', ascending=False)[columns_to_display]

#send outputs to terminal for testing
#print("\n")
#print(filtered_data)
#print("\n")
#print("Afinn Score From Comments Summary")
#print(data['afinn_score'].describe())

#output data to csv files
filtered_data.to_csv('reviews_pseudoanonymised_afinn_score_applied.csv')
data['afinn_score'].describe().to_csv('afinn_score_summary.csv')

#notify user script has finished processing
print("Sentiment Analyis completed - AFINN score applied")

