import pandas as pd
import numpy as np


def clear_text(region):
    if '(' in region:
        return region.split("(")[0].strip()
    elif '[' in region:
        return region.split("[")[0].strip()

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

out_list = []
current_st = ""
with open ("university_towns.txt","r+") as fh:
    for stname in fh:
        if "edit" in stname:
            current_st = stname.split("[")[0].strip()
        else:
            stname = clear_text(stname)
            out_list.append((current_st,stname))

df = pd.DataFrame(out_list, columns=["State","RegionName"])

df2 = pd.read_excel("gdplev.xls", skiprows=7)
df2 = df2[['Unnamed: 4', 'Unnamed: 5']] #Select column by index, (4,5,6) doesn't work

df2 = df2.loc[212:]
print(df2)

quarters = df2["Unnamed: 4"].tolist()
gdps = df2["Unnamed: 5"].tolist()

for idx in range(0,len(gdps)-1):
    try:
        if gdps[idx+2] < gdps[idx+1] < gdps[idx]:
            print(quarters[idx])
            break
    except IndexError:
        pass

"""
517,2
2008q3
2009q3
2009q2
"""

print("----------------------------------------")

start = 2000
end = 2016
qs = ["q1","q2","q3","q4"]
years = range(start,end+1)

quarters = [str(i)+j for i in years for j in qs]


q_dict = {"1":[1,2,3],
              "2":[4,5,6],
              "3":[7,8,9],
              "4":[10,11,12]}


def quarter_to_months(quarter):
    year,num = quarter.split("q")
    return [year+"-"+str(i).rjust(2,'0') for i in q_dict[num]]

def func(row):
    print("IN ROW")
    for quarter in quarters:
        row[quarter] = row[quarter_to_months(quarter)].mean()
    return row

df3 = pd.read_csv("City_Zhvi_AllHomes.csv")
df4 = df3.apply(func, axis=1)["2000q1"]
print(df4)