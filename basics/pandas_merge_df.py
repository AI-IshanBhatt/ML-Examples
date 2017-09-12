import pandas as pd
import numpy as np

purchase_1 = pd.Series({'Name':'Chris','Item Purchased':'Dog Food','Cost':22})
purchase_2 = pd.Series({'Name':'Martin','Item Purchased':'Cat Food','Cost':30})
purchase_3 = pd.Series({'Name':'John','Item Purchased':'Man Food','Cost':90})

df = pd.DataFrame([purchase_1, purchase_2,purchase_3], index=['Store1','Store1','Store2'])

df['Date'] = ["December 1","January 1","Mid-may"] #as long as length is same Here 3 or you can add scalar one as it will be broadcast
df["Feedback"] = ["Positive", None, "Negative"]

adf = df.reset_index() #Won't reset it as it returns a copy not view,you need to say inplace=True to make it work
                            #also, the index becl=omes a column name here
adf['Date'] = pd.Series({0:"December 1", 2:"January 1"}) #Add new column base on the index values
print(adf)

print("------------------MERGING DATAFRAME-----------------------------")
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'}, #Create df like this as well, list with same keys dicts
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

outer_joined = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print(outer_joined)
print()
inner_joined = pd.merge(staff_df, student_df, how='inner', left_index=True,right_index=True) #Must pass both
print(inner_joined)
print()
left_joined = pd.merge(staff_df, student_df,how='left', left_index=True, right_index=True)
print(left_joined)
print("---------------------JOIN WITHOUT INDEX----------------------------")
staff_df.reset_index(inplace=True)
student_df.reset_index(inplace=True)
non_index_merge = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name') #Then you provide column name of each side
print(non_index_merge)

print("--------------CONFLICTING ONES-------------------------")
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

merged_one = pd.merge(staff_df, student_df, how="outer", left_on="Name", right_on="Name")
print(merged_one) #loc_x loc_y are created to show which one belonged where
"""
Keep in mind if you have product_id as index in one and product_id as column in second (Very much possible)
merge using pd.merge(one, two, left_index=True, right_on="product_id")
Also you can join on multiple columns
pd.merge(one, two, left_on=["",""], right_on=["",""])
"""
print("----------------------USING APPLY--------------------------------")
def diff(row):
    diff = max(row) - min(row)
    return pd.Series({'diff':diff})

n = np.random.randint(10,30,12).reshape(4,3)
df1 = pd.DataFrame(data=n, columns=["a","b","c"])

df1["max"] = df1.apply(max, axis=1) #Simple max min can be done like this
df1["min"] = df1.apply(min, axis=1)
df1["mean"] = df1.mean(axis=1)
df1["diff"] = df1.apply(diff, axis=1) #Using user defined function here
df1["sum"] = df1.apply(lambda x: sum(x[["a","b","c"]]), axis=1) #Using lambda here itself
print(df1)

print("---------------------USING GROUPBY---------------------------------")
df1["gb"] = [1,1,2,2]
print(df1.groupby("gb").agg({"max":np.sum})) #agg takes dict, key-column name(s) val-Function to apply
print(df1.groupby("gb").size())
"""
If you want to groupby using index columns, you can do df1.groupby(level=0)
See soemthing interesting here
df.set_index("STNAME").groupby(level=0)["CENSUS2010POP"].agg({'avg':np.av},'max':np.max))
->Shows two new columns avg and max along with statenames that avg,max calculated on CENSUS2010POP
->This is groupby on series.

df.set_index("STNAME").groupby(level=0)['POPEST2010','POPEST2011'].agg({'avg':np.avg, 'max':np.max})
So when you run it you will get nice op/ with two headers avg, sum, then two columns that avg and max was calulated upon.
This is groupby on dataframe


SO either specify column name in agg or do a projection. Don't do both of them.
Especielly with dataframe groupby
"""

"""
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))


# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

One argument is implicit the df object itself. 2nd and 3rd are coumn names.
A new way of dealing YAY..

Doing projection on grouped by data. Selecting a and b columns
df.groupby("gb")["a","b"].agg({'max':np.max})

BEWARE,
If you do df.groupby("gb")["a","b"].agg({'a':np.max}), the original column would be replaced.
"""

print("--------SOME EXPERIMENT WITH CUT----------------")
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df5 = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
print(df5.head())

bins = [0, 25, 50, 75, 100] #Bins 0 to 25, 25 to 50 etc
group_names = ['Low', 'Okay', 'Good', 'Great']

categories = pd.cut(df5['postTestScore'], bins=bins , labels=group_names)
df5['Categories'] = pd.cut(df5['postTestScore'], bins=bins , labels=group_names)
print(df5)
"""
We created range (bins), the number of the ranges should be equal to lenght of group_names
then we categorise based on postTestScore and name the range as group_names.
"""

count = pd.value_counts(categories)
print("-------- With bins range-----------") #Specifies how many fit into the range(labels)
print(count)

print("----------------PIVOT TABLE--------------------")
pivot_df = pd.pivot_table(df5, index=['regiment', 'company'], aggfunc='mean') #Making these two as index and get mean over pre/postTestScore
print(pivot_df)
pivot_df1 = pd.pivot_table(df5, values='preTestScore', index='regiment', columns='company', aggfunc=[np.mean, len], fill_value=0)
"""
Above we specify which columns we need the aggfunc to be applied on by calling values=
columns= would provide different column names to data frame here, 1st 2nd Basically which company they belong to
index= the index on which the stuff needs to be done.
aggfunc is self explainatory
fill_value if Nan is fucking you
"""
print(pivot_df1)