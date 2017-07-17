import pandas as pd
import numpy as np

# Underneath panda stores series values in a typed array using the numpy library.
animals = ["Tiger", "Bear", "Moose"]
an_ser = pd.Series(animals)
print(an_ser)

numbers = [1,2,3,None]
num_ser = pd.Series(numbers)
print(num_ser) #None in number is stored as Nan -> Not a Number

print(np.nan==None) #Any comparison with nan is always false.
print(np.nan==np.nan)
print(np.isnan(np.nan)) #That's how you check NaN

#Let's create Series from dict, Here index is the key of the dict.
d = {"One":1,"Two":2,"Three":3,"Four":4}
d_ser = pd.Series(d)
print(d_ser)

#Getting the index object
print(an_ser.index)
print(d_ser.index)

print("------------QUERY SERIES-------------------")
sports = {"Archery":"Bhutan","Golf":"Scotland","Sumo":"Japan"}
s = pd.Series(sports)
print(s)
print(s.iloc[2]) #Querying index using index,rarely useful when index are name. s[3]
print(s.loc["Golf"]) #Makes more sense as weknow the index value here. s["Golf"]

print("----------------NON UNIQUE INDEX------------------")
cricket_loving_countries = pd.Series(["Aus","Barb","Pak"], index= ["Cricket", "Cricket", "Cricket"])
all_countries = s.append(cricket_loving_countries) #append returns a new one, original serieses are left as it is

print(all_countries) #Index can be non unique, that makes them different than Relational DB
print(all_countries.loc["Cricket"]) #Returns a series with index as Cricket