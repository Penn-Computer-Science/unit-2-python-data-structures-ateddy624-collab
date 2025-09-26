import pandas as pd
import random

fNames=["Mark", "Jimmy", "Andy", "Ben", "Calvin", "Conner", "James", "John", "Joe", "Timmy", "Billy", "Eli", "Ben", "Steven", "Marge", "Lisa"]
lNames=["Smith", "Jones", "Johnson", "Williams", "Brown", "Davis", "Rodrigues", "Miller", "Wilson", "Moore"]
years=["Freshman", "Sophmore", "Junior", "Senior", "Victory Lap"]
pathways=["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Child Education", "Culinary", "Criminal Justice", "Construction", "Bio Med"]
names=[]

for i in range(20000):
    names.append(f"{random.choice(fNames)}  {random.choice(lNames)}")

data={
    "Name":names,
    "Age": [random.randint(14,19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)

pennData.to_csv("pennData.csv", index=False)

#print(pennData)