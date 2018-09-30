import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import  csv, re, json
import pandas as pd
from nltk.metrics import edit_distance
from nltk.corpus import opinion_lexicon
import numpy as np

df= pd.read_csv("data22C.txt", sep='\t', names=['tweetid','topic','sentiment','tweet1'])
data = df.tweet1

"""   
with open("2016-part2-subtaskBD.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    data =[]
    for line in tsvreader:
        data.append(line)       
"""
tweets = []
tweets1 =[]
#replace upper case letters with lower case
def replaceCapitals(tweet):
    for i,t in enumerate(tweet):
        tweets.append(str.lower(t))
        #tweets1= re.sub(r"http\S+|www\S+", "*URL*", tweets)
    return tweets

#function calling to replace the  upper_case data with lower_case
 
#replace URLs with "*URL*"        
def replaceURLs(tweet):
    for i, t in enumerate(tweet):
        tweets[i] = re.sub(r"http\S+|www\S+", "*URL*", t)
    return tweets      

#function calling to replace the original data with "*URL*"

x = replaceCapitals(data)
y = replaceURLs(x)

#replace hashtags with "*HASHTAG*" 
def replaceHashtags(tweet):
    for i, t in enumerate(tweet):
        tweets[i] = re.sub("(#[A-Za-z0-9_]+)", "*HASHTAG*", t)
    return tweets

#function calling to replace the  data with "*HASHTAG*"

z = replaceHashtags(y)
  
#replace user tagging with "*USERTAGGING*"
def replaceUserTagging(tweet):
    for i, t in enumerate(tweet):
        tweets[i] = re.sub("(@[A-Za-z0-9_]+)", "*USERTAGGING*", t)
    return tweets    

#function calling to replace the  data with "*USERTAGGING*"
u = replaceUserTagging(z)
    
"""
#replace emoticons with "*EMOJIS*" 
def replaceEmojis(tweet):
    emoticon_string=r"[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|\\]|[\)\]\(\[dDpP/\:\}\{@\|\\][\-o\*\']?[:;=8][<>]?"
    for i, t in enumerate(tweet):
        if re.match(emoticon_string, t):
            tweet[i]="*EMOJIS*"
    return tweet 

#function calling to replace the  data with "*EMOJIS*"
for l in data:
    replaceEmojis(l) 
""" 
def elongatedData(tweet):
    for i,t in enumerate(tweet):
        tweets[i] = re.sub(r'(.)\1+',r'\1\1',t)
    return tweets    


qq = elongatedData(u) 
 
def tokeni(tweet):
    for i, t in enumerate(tweet):    
        tweet[i] = word_tokenize(t)
    return tweet

ww = tokeni(qq)
    
def pos(tweet):
    for i, t in enumerate(tweet):    
        tweet[i] = nltk.pos_tag(t)
    return tweet
    
pos(ww)

#print(tweets)

df1 = pd.DataFrame({"tweet2" : tweets})
#print(df1)

df['tweet1'] = df1['tweet2']
np.savetxt('data24C.txt', df.values, fmt='%s', delimiter="\t")
