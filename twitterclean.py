import pandas as pd 
import numpy as np 


df = pd.read_csv('/Users/hishammohamedabdelaal/Desktop/Ahmed Stuff/Data Science Project/Twint_2nd_assignment/arsenal.csv')
print(df.head())


use = df[[
    'username',
    'tweet',
    'likes_count',
    'retweets_count',
]]

print (use.head())

use.to_csv('CleanArsenal.csv', sep = '\t')



