import numpy as np
import time

"""list1 = range(10000000)
list2 = range(10000000)
starting_time=time.time()
list3 = [(a*b)for a,b in zip(list1,list2)]
print("time taken for list operation is",time.time()-starting_time)

array1=np.arange(10000000)
array2=np.arange(10000000)
initial_time=time.time()
array3=array1*array2
print("Time taken by arrayoperation is",time.time()-initial_time)"""

zeroes_array= np.zeros((3,3))
print(zeroes_array)

empty_array = np.empty((5,3))
print(empty_array)
#print(zeroes_array)

arange_example=np.arange(10,20,3)
print(arange_example)