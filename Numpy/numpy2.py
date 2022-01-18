import numpy as np

arr1 = np.arange(101)
arr2 = arr1[arr1 % 2 != 0]
arr1 = np.where(arr1 % 2 != 0, -1, arr1)
print(arr1, arr2, sep='\n\n')