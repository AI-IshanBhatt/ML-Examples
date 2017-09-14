
import pandas as pd
import numpy as np


def cleanup(row):
    """
    row - It is a series
    row[0] - it is first column, here country name
    So, we'll check row[0] for country names , 1,2,3 for ...
    """
    row[0] = cleanup_country(row[0])
    row[1] = np.nan if row[1] == "..." else row[1]
    row[2] = np.nan if row[2] == "..." else row[2]
    row[1] *= 1000000
    return row #You got to return the row to have your changes reflected Otherwise useless


def cleanup_country(country_name):
    """
    We'll just fuck around with country name here.
     ... values would be taken care by replace method directly on the coulumn
    """
    if '(' in country_name:
        country_name = country_name.split("(")[0].strip()
    if not country_name.isalpha():
        country_name = ''.join([i for i in country_name if not i.isdigit()])
    return country_name


df = pd.read_excel(r'C:\Users\SONY\Downloads\Energy Indicators.xls', skiprows=17, skip_footer=38)
df.drop(df.columns[[0, 1]], axis=1, inplace=True)
df.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
# print(df['Energy Supply'].where(df['Country'] == 'American Samoa')) #This shit returns a whole series  we need only one

#Easy way to do - select column1 where column2='abc'
print(df.loc[df['Country'] == 'American Samoa', "Energy Supply"])

#Easy way to do - select column1 where column2 in [1,2,3]
print(df.loc[df['Country'].isin(['American Samoa','Zimbabwe']), "Energy Supply"])

#Easy way to do - select column1,column2 where column2 in [1,2,3]
print(df.loc[df['Country'].isin(['American Samoa','Zimbabwe']), ["Energy Supply", "Country"]])

#Select *  where column2 in [1,2,3]
print(df.loc[df['Country'].isin(['American Samoa','Zimbabwe'])])

country_dict = {"Republic of Korea": "South Korea",
                "United States of America20": "United States",
                "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
                "China, Hong Kong Special Administrative Region3": "Hong Kong"}

# df["Energy Supply"] *= 1000000 We'll put it afterwards ,after cleaning the data
df['Country'].replace(country_dict, inplace=True)
print(df.loc[df['Country'].isin(['South Korea', 'United States', 'United Kingdom','Hong Kong'])])
print()
print()
print("-------------APPLY TO CLEAN DATA---------------")
df3 = df.apply(cleanup, axis=1)
print(df3.head())
print()
print()
print(df3.loc[df3['Country'] == 'Switzerland'])
print(df3.loc[df3['Country'] == 'Bolivia'])
# print(df3.loc[0]) #That's how you search fromindex in case you have forgotten

print("---------------------Cleaning the data column wise----------------------")
df4 = df.copy()
df4["Country"] = df4["Country"].apply(cleanup_country)
nan_dict = {"..." : np.nan}
df4["Energy Supply"].replace(nan_dict, inplace=True)
df4["Energy Supply per Capita"].replace(nan_dict, inplace=True)
print(df4.head())

print("-------------------CLEANING THE GDP DATA-------------------------------")
df6 = pd.read_excel(r'C:\Users\SONY\Downloads\API_NY.GDP.MKTP.CD_DS2_en_excel_v2.xls', sheetname="Data", skiprows=3)
country_dict = {"Korea, Rep.": "South Korea",
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}
df6["Country Name"].replace(country_dict, inplace=True)
print(df6.loc[df6['Country Name'].isin(["South Korea","Iran","Hong Kong"])])

print("------------------CLEANING scimagojr DATA----------------------------")
df7 = pd.read_excel(r'C:\Users\SONY\Downloads\scimagojr.xlsx')
print(df7.head())

print("-----------------LETS JOIN THE SHIT-----------------------------------")
#df3, df6 df7
df6.rename(columns={"Country Name":"Country"}, inplace=True) #Using rename to change column name
year_columns = list(map(str, [i for i in range(2006,2016)])) #Keepit cool stuff
df8 = pd.merge(pd.merge(df3, df6, on="Country", how='inner'), df7.loc[df7["Rank"] < 16], how='inner', on='Country')
#Above is triple merge, and we are picking only those from df7 whose rank is less than 16 in the merging.
#Could have used df1.merge(df2[list('xab')]) if we wanted to use only x,ab columns of df2 in the merging
#Thought of using it that's why created year_column
my_coulumns = ['Country','Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document',\
               'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',\
               '2009', '2010', '2011', '2012', '2013', '2014', '2015']
df8 = df8[my_coulumns]
df8.set_index('Country', inplace=True) #Setting the index, as simple as that
print(df8.head())
print(df8.index)