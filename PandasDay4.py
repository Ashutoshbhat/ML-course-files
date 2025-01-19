import pandas as pd
titanic_def=pd.read_csv("titanic.csv")
#print(titanic_def.head())

print(titanic_def.shape)
#shape tells us how many rows and columns there are in the file

print(titanic_def.info())
#It tells us all about the columns of the file or table

print(titanic_def.describe())
# It tells us all about the columns data i.e mean, count, std, min,max,25%,50%,75% etc

"""print(titanic_def[100:200])

print(titanic_def.columns)

titanic_def.set_index("PassengerId",inplace=True)
print(titanic_def[["Name","Age"]])

#print(titanic_def[(titanic_def["Age"]>30) & (titanic_def["Survived"]==1)])"""
 