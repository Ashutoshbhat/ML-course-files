import pandas as pd
dict_list1 ={
    "Names":["Taran","Anil","Vansham","Aman","Pranwat"],
    "Ages":[18,18,19,18,17],
    "Marks":[95,72,88,80,88],
    "City":["Jammu","Srinagar","Delhi","Jammu","Delhi"]
}
students_df1=pd.DataFrame(dict_list1)
#students_df1=students_df1.set_index("Names")
students_df1.set_index("Names",inplace=True)
print(students_df1.loc['Taran'])

#grouped_df1=students_df1.groupby("City")
#print(grouped_df1.get_group("Jammu"))

#grouped_df1=students_df1.groupby("City").sum()
#print(grouped_df1)

#grouped_df1=students_df1.groupby("City").mean()
#print(grouped_df)

dict_list2 ={
    "Names":["Tarandeep","Anil Kumar","Vansham Angral","Amanveer","Pranwat Singh"],
    "Ages":[118,118,119,118,117],
    "Marks":[195,712,818,810,188],
    "City":["Jammu","Srinagar","Delhi","Jammu","Delhi"]
}

students_df2=pd.DataFrame(dict_list2)
students_df2=pd.merge(students_df1,students_df2,on="Names",how="left")
print(students_df2)

#grouped_df1=students_df1.groupby("City").agg("mean","std","sum")
#print(grouped_df1.get(0))

"""Homework is to merge two dataframes with mostly different details but just a single similar column so it can become a primary key to make our work easier."""

#to particulary select a condition i.e if we want the marks above 90
print(students_df1[students_df1['Marks']>90])

# we can also add multiple conditions in one statement
print(students_df1[students_df1['Marks']>90],[students_df1["Ages"]>18])
