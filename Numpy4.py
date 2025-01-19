import numpy as np
arr1=np.random.randint(3,9,(30,5))
print(arr1)
#arr2=arr1.flatten()
#print(arr2)
#arr2=arr1.flatten(order='F')
#print(arr2)
print(arr1.reshape(-1,30).shape)

arr2=np.insert(arr1,2,[5,6,7],axis=0)
print(arr2.shape)