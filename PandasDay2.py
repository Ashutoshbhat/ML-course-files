import pandas as pd
list_dicsts=[
    {'name':'arun','age':22,'address':'jammu'},
    {'name':'puja','age':22,'address':'samba'},
    {'name':'aman','age':22,'address':'Kunjwani'}
    ]
print(list_dicsts)

dict_lists={'name':['taran','karen','aman','anil'],
            'age':[22,28,99,19],
            'address':['jammu','samba',"jammu",'mumbai']
            }

pdf =pd.DataFrame(list_dicsts)
print(pdf)

'''aman = pd.DataFrame(dict_lists)
print(aman)'''

dict_lists_df=pd.DataFrame(dict_lists)
dict_lists_df.columns=['names','student_age','location']
dict_lists_df=dict_lists_df.set_index('names')
print(dict_lists_df.loc[['taran',"aman"],['student_age','location']])
      