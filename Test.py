import pandas as pd

import numpy as np


df = pd.read_csv('/Users/jonathanlai/Downloads/CorrectFinalMaskOff.csv')


Young = df[df['age'] == "<=18"]
Middle = df[df['age'] == "19-29"]
Old= df[df['age'] == "30-39"]
VeryOld = df[df['age'] == ">40"]



Df1 = pd.concat([Young.sample(n=7500),Middle.sample(n=7500),Old.sample(n=5000),VeryOld.sample(n=5000)])

print(Df1.id)


print(list(Df1.id))



