import twint 
import pandas as pd
import numpy as np 


c = twint.Config()
c.Search = ''
c.Limit = 40000

c.Pandas =True

c.Lang= 'en'


c.Store_csv = True
c.Output= "arsenal.csv"

#twint.run.Search(c)



