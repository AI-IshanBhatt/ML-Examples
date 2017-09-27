
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.5** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas
# This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, 
# 
# e.g. 
# 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# 
# `'Switzerland17'` should be `'Switzerland'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[2]:

import pandas as pd
import numpy as np

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

def cleanup(row):
    """
    row - It is a series
    row[0] - it is first column, here country nameenergy = pd.read_excel("Energy Indicators.xls",.....
GDP = pd.read_csv('world_bank.csv',....
ScimEn = pd.read_excel('scimagojr-3.xlsx')
    So, we'll check row[0] for country names , 1,2,3 for ...
    """
    row[0] = cleanup_country(row[0])
    row[1] = np.nan if row[1] == "..." else row[1]
    row[2] = np.nan if row[2] == "..." else row[2]
    row[1] *= 1000000
    return row

def answer_one():
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, skip_footer=38)
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    country_dict = {"Republic of Korea": "South Korea",
                "United States of America20": "United States",
                "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
                "China, Hong Kong Special Administrative Region3": "Hong Kong"}
    energy['Country'].replace(country_dict, inplace=True)
    energy = energy.apply(cleanup, axis=1)
    
    country_dict = {"Korea, Rep.": "South Korea",
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}
    GDP["Country Name"].replace(country_dict, inplace=True)
    GDP.rename(columns={"Country Name":"Country"}, inplace=True)
    merged = pd.merge(pd.merge(energy,GDP,on="Country", how="inner"),ScimEn.loc[ScimEn["Rank"] < 16], how="inner", on="Country")
    my_columns = ['Country','Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document',               'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',               '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    merged = merged[my_columns]
    merged.set_index("Country", inplace=True)
    return merged



# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[1]:

get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[8]:

def answer_two():
    return 156


# <br>
# 
# Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[13]:

def answer_three():
    Top15 = answer_one()
    last_ten = list(map(str, range(2015,2005,-1)))
    avg_gdp_10 = Top15[last_ten].fillna(0).apply(lambda row: sum(row),axis=1)
    return  avg_gdp_10.sort_values(ascending=False) #As index is country you are getting two in Series

print(answer_three())


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[56]:

def answer_four():
    Top15 = answer_one()
    last_ten = list(map(str, range(2015,2005,-1)))
    sixth_avg = Top15[last_ten].mean(axis=1).sort_values(ascending=False).index[5]
    difference = Top15.loc[sixth_avg]["2015"] - Top15.loc[sixth_avg]["2006"]
    return difference


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[58]:

def answer_five():
    Top15 = answer_one()
    mean_energy = Top15["Energy Supply per Capita"].mean()
    return mean_energy


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[71]:

def answer_six():
    Top15 = answer_one()
    max_ren = Top15["% Renewable"].idxmax()
    return (max_ren, Top15.loc[max_ren]["% Renewable"])


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[19]:

def answer_seven():
    Top15 = answer_one()
    Top15["ratio"] = Top15["Self-citations"] / Top15["Citations"]
    max_ratio = Top15["ratio"].idxmax()
    return (max_ratio, Top15.loc[max_ratio]["ratio"])


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[5]:

def answer_eight():
    Top15 = answer_one()
    Top15["est_pop"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    third_pop_country = Top15["est_pop"].sort_values(ascending=False).index[2]
    return third_pop_country


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[ ]:

def answer_nine():
    Top15 = answer_one()
    return "ANSWER"


# In[ ]:

def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[ ]:

#plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[19]:

def answer_ten():
    Top15 = answer_one()
    Top15 = Top15.sort_values(by="Rank", ascending=True)
    Top15["HighRenew"] = np.where(Top15['% Renewable'] >= Top15['% Renewable'].median(), 1, 0)
    return Top15["HighRenew"]


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[14]:

def answer_eleven():
    Top15 = answer_one()
    Top15["Population"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    grouped_df = Top15.groupby(ContinentDict)["Population"].agg({'size':"size",'sum':np.sum,    'mean':np.mean,'std':np.std})
    return grouped_df

answer_eleven()


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[ ]:

def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[21]:

def answer_thirteen():
    Top15 = answer_one()
    Top15["Population"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    thousands = Top15["Population"].map('{:,}'.format)
    return thousands

print(answer_thirteen())


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[ ]:

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!

