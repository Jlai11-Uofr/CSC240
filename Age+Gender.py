#Property of Jonathan Lai
import csv
from m3inference import M3Inference
from m3inference import M3Twitter
import pprint
import jsonlines
import time
import re
import bigjson
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from spellchecker import SpellChecker
import nltk

import pandas as pd
import numpy as np

#Basic imports
##We also need to process the tweet
def _processTweet(tweet):
    spell = SpellChecker()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
    pattern = re.compile(r"(.)\1{2,}")
    tweet = pattern.sub(r"\1\1", tweet)
    tweet = word_tokenize(tweet)

    misspelled = spell.unknown(tweet)

    for word in misspelled:
        tweet = [spell.correction((word)) if x == word else x for x in tweet]
    String= ''
    for item in tweet:
        String = String+item+" "
    return String

time1 = time.time()
m3twitter=M3Twitter(cache_dir='twitter cache') #Change the cache_dir parameter to control where profile images are downloaded
analyzer = SentimentIntensityAnalyzer()
from m3inference import M3Inference
import pprint
Columns = ['Tweet_id',"name",'id','location','text','sentiment','age','gender','date','time','race','score','screen_name']
df= pd.DataFrame(columns= Columns)


m3 = M3Inference()


with jsonlines.open('/Users/jonathanlai/Downloads/501.jsonl') as f:
    count = 0
    listx = []

    for line in f.iter():

        try:
            text = line['retweeted_status']['full_text']
            text = _processTweet(text)
        except:
            try:
                text = line['full_text']
                text = _processTweet(text)
            except:
                continue



        count = count+1
        print(count)
        if(line['lang'] == 'en') and (re.search("(mask|N-95|n95)", text, re.IGNORECASE)) :
            print(text)
            S = line['created_at'].split(" ")
            x = str(line['id'])
            S1 = S[1] +S[2]
            S2=S[3]



            listx.append(line)
            #df = df[df['full_text'].str.contains('mask|facemask|face mask|N-95', regex=True, flags=re.IGNORECASE)]



            vs = analyzer.polarity_scores(text)['compound']

            if (float(vs) >= .05):
                score = (vs)
                sentiment = "Positive"

            elif (float(vs) <= -.05):
                score= (vs)
                sentiment  = 'Negative'

            else:
                score = (vs)
                sentiment = 'Neutral'
            print(sentiment)
            df = df.append(
                {"sentiment": sentiment, "Tweet_id": x, "name": str(line['user']['name']), 'id': line['user']['id_str'],
                 "text": text,
                 "location": line['user']['location'], 'date': S1, 'time': S2,'score': score,"screen_name" :line['user']['screen_name']}, ignore_index=True)

            #print("eng")

        else:
            pass



df.to_csv('Lastsday.csv')

list1 = []

count = 0



for item in listx:
  count = count+1
  try:


        x = m3twitter.transform_jsonl_object(input=item)
        print(count)


        list1.append(x)




  except:
      pass



for item in list1:
            list2 = []
            list2.append(item)

            try:
                print(item)
                pred = m3.infer(list2,output_format= 'dataframe')

                if(pred.loc[0,'gender_male'] > pred.loc[0,'gender_female']) :
                   gender = 'Male'
                else:
                   gender ='Female'

                if(pred.loc[0,'age_>=40'] > .5):
                    age = ">40"
                elif (pred.loc[0, 'age_<=18'] > .5):
                    age = '<=18'
                elif (pred.loc[0, 'age_19-29'] > .5):
                    age ='19-29'
                elif (pred.loc[0,'age_30-39'] > .5):
                    age = '30-39'

                else:
                    print("Unclear_Gender")


                if(pred.loc[0,'org_is-org'] > .8):
                    org = 'yes'
                else:
                    org = 'no'

                print(pred)
                Index_label = df[df['id'] == str(item['id'])]


                df.loc[Index_label.index,'gender'] = gender
                df.loc[Index_label.index, 'age'] = age

                print(df.loc[Index_label.index])




            except:
                pass
                print("Broken")

df.to_csv('Muqing.csv')


time2= time.time()


print(str(time2-time1))




