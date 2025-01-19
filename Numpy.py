import numpy as np
import sys
list_example=range(10)
array_example=np.arange(10)
print(sys.getsizeof(list_example)*len(list_example))
print(array_example.itemsize*array_example.size)

list1 = np.random.randint(1000)
list2 = np.random.randint(1000)

array1 = np.array(list1)
array2 = np.array(list2)
list_comprehension=[1,2,3,4,5,6]
#list_comprehension=[x*x for x in list_comprehension]
#list3 = [a*b for a,b in zip(list1,list2)]
new_list=[]
for i in range (len(list_comprehension)):
    #new_list[i]=list_comprehension[i]**2
    new_list.append(list_comprehension[i]**2)
print(new_list)
list_transformed=[x**2 for x in list_comprehension if x%2==0]
print(list_transformed)