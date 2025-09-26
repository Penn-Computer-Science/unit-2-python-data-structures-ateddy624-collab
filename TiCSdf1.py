import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#Load our dataframe
df=pd.read_csv('pennData.csv')
pennData=pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe")  #first five rows of the dataframe
print(pennData.head())

print("-_"*20)
print("Tail of the Dataframe")  #last five rows of the dataframe
print(pennData.tail())

print("-_"*20)
print("Summary of the Dataframe")  #summary of the dataframe
print(pennData.info())

print("-_"*20)
print("Statistical Analysis of the Dataframe")  #statistical analysis of the dataframe
print(round(pennData.describe(),2))

print("-_"*20)
print("Count of students in pathways")  #count of students in each pathway
print(pennData["Pathway"].value_counts())

print("-_"*20)
print("Average GPA Per Year")  #Average GPA per year
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top 3 Students by GPA")  #Top 3 Students by GPA
print(pennData.sort_values(by='GPA',ascending=False).head(3))

print("-_"*20)
print("Students with GPA.3.5")  #Students with GPA.3.5
print(pennData[pennData['GPA']>3.5])

print("-_"*20)
print("First Student Data")  #First Student's Data
print(pennData.iloc[0])