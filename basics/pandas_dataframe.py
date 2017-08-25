import pandas as pd

purchase_1 = pd.Series({'Name':'Chris','Item Purchased':'Dog Food','Cost':22})
purchase_2 = pd.Series({'Name':'Martin','Item Purchased':'Cat Food','Cost':30})
purchase_3 = pd.Series({'Name':'John','Item Purchased':'Man Food','Cost':90})

df = pd.DataFrame([purchase_1, purchase_2,purchase_3], index=['Store1','Store1','Store3']) #Opposed to relational one, it can have same index, Keys become COLUMN names

print(purchase_1.index) #As from previous class,index are the key of the dict.
print(df.head()) # Always print df with head as in future you will have huge df , so you can see the structure like this

print(df.loc['Store1'])
print(df.loc[df['Cost']==90].index.format())
print(type(df.loc['Store3'])) #type is series in case of 1 row, dataframe in case of more than 1 row with that index

print("---------------------SOME TRICKERY----------------------------")
print(df.loc['Store1', 'Cost']) #Rowindex-Store1, ColumnIndex-Store
print(df['Cost']) #That's how you get column projection, Selectin single column,
print(df[['Cost','Name']]) #That's how you select multiple columns, passing list to []
print(df.loc[:,['Cost','Name']]) #Same as above using loc
"""
print(df.loc['Store1']['Cost'])
This is called chain operation, as loc returns df or series
It's better to avoid it as much as possible as  In particular, chaining tends to cause Pandas to return a copy of the DataFrame instead of a view on the DataFrame.
"""

""" KEEP IN YOUR GODDAMN MIND
Also, df.loc['Cost'] will not work as loc and iloc only works on index, here index is Store1,3
Also, don't attempt df['Series1','Cost'] as df[] knows only about it's data not the index.
"""
df1 = df.drop('Store1') #Here the original df won't be affected, instead it returns a copy,ou can specify inplace=True to change original one
print(df1)

#A common pattern to drop stuff, don't use inplace unless it's absolutely necessary
copy_df = df.copy()
copy_df = copy_df.drop('Store3')
print(copy_df)

#axis=1 for column deletion,off course you need to provide the column name at that time
print("REMOVING COLUMN")
df2 = df.drop('Cost',axis=1)
print(df2)

#Another way to delete column, this doesn't return a copy. Instead deletion happens immedietely and inplace
del copy_df['Cost']

print("ADDING A NEW COLUMN")
df["Location"] = "NY" #This broadcasts new value to all rows.
print(df)

print("---------------------DATA FRAME INDEXING AND LOADING-----------------------")
costs = df["Cost"]
costs += 10
print(df) #Original df gets changes, so df['Cost'] returns view not copy
"""
df = pd.read_csv(path, index_col = 0, skip_rows=1)
"""
print("----------------------Querying DATAFRAME-------------------------------")
country_df = pd.read_csv("Olympics.csv", index_col=0)
print(country_df)
print("------------------------BOOLEAN MASK----------------------------------")
countries_gold = country_df["Golds"] > 0 #We built our boolean mask, We'll apply it on df using where
"""
The where function takes a Boolean mask as a condition,
applies it to the DataFrame or series, and returns a new DataFrame or series of the same shape.
"""
# print(countries_bronze) #This just gives the index-TruthValue value Series
print("---------------------------------")
only_golds = country_df.where(country_df["Golds"] > 100) #The countries with false result of boolean mask will have Nan
print(only_golds.head()) #Print that dataframe, previously not working maybe because of where returns copy not view
print(only_golds["Golds"].count()) #Find number of countries with more than 100 golds

"""
We don't need where function explicitly. The indexing operator can take boolean mask
There is no NaN when you do things like this.
"""
print("------------------USING INDEX NOT WHERE----------------------")
only_golds = country_df[country_df["Golds"] > 100] #Very concise,also AND OR operators can be used
print(only_golds["Golds"])
"""
When using index operator as where, try to keep it as last one if you are chaining
df['Name'][df['Cost'] > 10] and as you must have noticed, WHERE
df[df["cost"] > 10]["Name"] or df["Name"][df["cost"] > 10], both works as 
SELECT NAME FROM DF WHERE COST > 10;
"""
print(country_df[(country_df["Golds"] > 100) | (country_df["Bronzes"] > 400)]) #Each boolean mask needs to be in () because of ordering of operators

print("-------------------Indexing DataFrames----------------------")
"""
Do it using set_index, but it doesn't preserve orignal index
So you need to save original index into a column and then create a new index from existing column
"""
df = country_df.copy();
df["Country"] = df.index;
df = df.set_index("Golds") #This may seem BS as it's an operation but it returns the copy not view so you need to assign it
                        #back to the orignal one to have reference updated
print(df.head())
print(type(df['Silvers']*2))
"""
df = df.reset_index(), can remove the current index and makes orignal numeric values as index.
"""

"""
You can create multi level index as well using the same set index
df = df.set_index(["c1","c2"]),it will be a composite key like db
Also you can do df["Golds"].unique()
"""

"""
Update index example
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name'] Setting names to index
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn'))) Append using series
data - Store the value for data , name - Store the values for index
"""
print("---------------------ASSIGNMENT ANSWERS COMMENTS----------------")
"""
KEEP IN MIND,
if you set_index in a function reset_index in that function itself.
Otherwise Jyupiter will fuck you around.
WHEN IN DOUBT , RELOAD THE KERNEL
def answer_five():
    max_count_id = census_df.groupby("STATE").count().idxmax()['STNAME']
    return ''.join(census_df['STNAME'][census_df['STATE'] == max_count_id].unique())
answer_five()

def answer_five():
    max_count_id = census_df.groupby("STNAME").size().idxmax() #This idxmax corresponds to the STNAME not the original index.
    #As the index now would be STNAME the one on which grouped by.
#     Also,when yyou want number of rows per group use sizenot count. SO you won't need a projection on a column again after you
#     did with count.
    return max_count_id
answer_five()
"""
