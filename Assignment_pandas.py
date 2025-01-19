import pandas as pd
from datetime import datetime, timedelta
list_dicsts=[
    {'name':'arun','age':22,'Roll no':'12','marks':'89'},
    {'name':'puja','age':25,'Roll no':'13','marks':'97'},
    {'name':'aman','age':27,'Roll no':'12','marks':'99'}
    ]
a=pd.DataFrame(list_dicsts)
b=(a["age"])
c=(datetime.now()-pd.to_timedelta(b*365,unit="d"))
# new_date=c.strftime('%d/%m/%Y')
# print(new_date)
csv_filename ='studentdetails.csv'
c.to_csv("C:\\Users\\HP\\Downloads\\assignment2.csv", index=False)
print("File exported")


# student={'name':['Prince','Manu'],'rollno':[1,2],'age':[20,25]}
# import pandas as pd
# from datetime import datetime, timedelta
# print(student)
# student_df=pd.DataFrame(student)
# print(student_df)
# print(student_df['age'])
# student_date= pd.to_datetime('2024-05-05') 
# student_df["dob"]= student_df["age"].apply(lambda x:student_date- timedelta(days=x*365))
# print(student_df['dob'])
# csv_filename = 'student_details.csv'
# student_df.to_csv("C:\\Users\\HP\\Downloads\\student_details.csv", index=False)
# print(csv_filename,"exported")