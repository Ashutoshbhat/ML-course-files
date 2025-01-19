import pandas as pd
import numpy as np
"""list_rolls = [2,3,4,5,6]
print(type(list_rolls))
print(list_rolls)

series_roll = pd.Series(list_rolls, name="Roll_no.")
print(type(series_roll))
print(series_roll)

list_of_lists = [[1,2,3,4,5],['a','b','c','e']]
print(pd.Series(list_of_lists))"""

array1 = np.random.randint(3,9,(3,3))
print(array1)

df1 = pd.DataFrame(array1,columns=['a','b','c'])
print(df1)
print(df1['b'])


'''dict_students = {'Names':['Taran','Aman','Harsh'],'Roll_no.':[16,48,70]}
print(dict_students)
dict_students_df = pd.DataFrame(dict_students)
print(dict_students_df)'''