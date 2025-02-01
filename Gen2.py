import pandas as pd
import numpy as np
csvFile = pd.read_csv('DQ2.csv')
print(csvFile)


#Colomn Addition(Language)

b=pd.DataFrame(csvFile)
c=b.copy()
print(c)


#Colomun Change


c['Email'][1]='sundaymood@gmail.com'
print(c['Email'][1])
print(c)
c["Language"] = pd.Series([
    "Java", "Python", "R", "C", "C++", "Ruby", 
    "Java", "Java", "Python", "R", "C", "C++", "Ruby",
    "C", "C", "C++", "Java", "Python", "Java", "Python",
    "R", "C", "C++", "Ruby", "R", "Java", "Python", "Java",
    "Python", "R", "C", "C++", "Ruby", "Java", "Python",
    "R", "C", "C++", "Ruby"])
print(c)
print("***********")

#Row Addition( Kaal Bhairav)


r={'Index':40,'Customer':'08gq4384ts','First_Name':'Kaal','Last_Name':'Bhairav',
   'Company':'Rudra','City':'Kaashi','Country':'India','Phone_1':562419469,
   'Phone_2':2310561238,'E-mail':'kaashika@gmail.com','Subscription':1/26/2022,
   'Website':'Kaashitourism'}
c=c.append(r,ignore_index=True)
print(c)


#Column Selection

print(c['Email'])
print(c['City'][5])

#Row Selection

print(c.loc[0])
print(c.loc[0][1])


#Row Change
c.loc[0,'First_Name']='Praboss'
print(c)


#Column Deletion

c.pop('Website')
print(c)

#Row Deletion

d=c.drop(37)
print(d)



