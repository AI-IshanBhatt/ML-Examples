import pandas as pd
import numpy as np

t1 = pd.Timestamp('12/23/2016 08:56AM')
print(t1)

p1 = pd.Period('3/2017') #Month period
print(p1)

p2 = pd.Period('3/4/2017') #Day Period
print(p2)

s1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print(s1)
print(s1.index) #It is a DatetimeIndex

s2 = pd.Series(list('def'), [pd.Period('2016-10'), pd.Period('2016-11'), pd.Period('2016-12')])
print(s2)
print(s2.index) #It is period index

print("------------CONVERTING TO DATAFRAME------------------")
d1 = ['2 June 2013', 'Aug 29 2014', '2015-06-26', '7/12/2016']
ts3 = pd.DataFrame(np.random.randint(10,20,(4,2)), index=d1, columns=list('ab'))
print(ts3)
ts3.index = pd.to_datetime(ts3.index) #Converting it into correct date frommultiple date formats
print(ts3)

"""
If you dont like month first you can do pd.to_datetime('4.7.12', dayfirst=True)
"""
print("---------------TIME DELTAS--------------------------")
x = pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')
print(x)
y = pd.Timestamp('9/2/2016 8:10AM') +pd.Timedelta('12H 3D')
print(y)

print("------------Dates in DATA FRAME--------------------")
dates = pd.date_range('10-01-2016', periods=9, freq="2W-SUN")
df = pd.DataFrame({'Count1' : 100 + np.random.randint(-5,10,9).cumsum(),
                   'Count2' : 120 + np.random.randint(-5,10,9)}, index=dates)
"""
Above thing works even if the index isn't specified it would create df on 9 values with count1 and count2
"""
print(df)

print("------Resample shit here too---------") #Month wise
print(df.resample('M').mean())
print("-------Partial Serarches with dates-----------")
print(df['2017'])
print(df['2016-11'])
print(df['2016-12':])

print("-------------CHANGING THE FREQUENCY------------")
df1 = df.asfreq('w', method='ffill') #It fills up the in between with the prevos one
print(df1)

