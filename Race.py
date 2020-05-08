import re
from ethnicolr import census_ln, pred_census_ln, pred_wiki_name
import tensorflow
import pandas as pd
from sklearn import preprocessing
import csv
import pandas as pd
import ethnicolr
from ethnicolr import pred_wiki_name
from collections import OrderedDict
from nameparser import HumanName

import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ekphrasis.classes.segmenter import Segmenter

analyzer = SentimentIntensityAnalyzer()

count = 0
pd.set_option('display.max_columns', None)
sentence = 'Pleaase if you are going outside remmebr to wear a n95'
names = [{'name': 'fan', 'first': 'muqing'},
         {'name': 'Amaral', 'first': 'jenkins'},
         {'name': 'lai', 'first': 'jenkins'}]

label_encoder = preprocessing.LabelEncoder()


# df = pd.DataFrame(names)
# print(df)
# print(pred_wiki_name(df, 'first','name'))
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


Path = 'Muqing.csv'
df = pd.read_csv(Path)
listx = []
for index, row in df.iterrows():
    count = count + 1
    Dirtyname = row['name']
    print(Dirtyname)
    Clean = deEmojify(str(Dirtyname))
    Testname = HumanName(Clean)

    if len((Testname.last)) == 0:
        First = Testname.first
    if (len(Testname.first)) == 0:
        Last = Testname.last

    if len(Testname.last) == 0 and len(Testname.first) == 0:
        continue



    else:
        First = Testname.first
        Last = Testname.last
        hmm = [{'First': First, 'Last': Last}]
        print(count)
        gg = pd.DataFrame(hmm)
        pred = (pred_wiki_name(gg, 'First', 'Last'))
        x = str(pred.loc[0, 'race'])
        df.loc[index, 'race'] = x
        print(df.loc[index, 'race'])

df.to_csv("Abc.csv")
