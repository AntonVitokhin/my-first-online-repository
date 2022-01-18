import numpy as np

arr1d = np.arange(10, 110)
arr2d_1 = arr1d.reshape(20, 5)
arr2d_2 = arr1d.reshape(5, 20)
print(arr1d, arr2d_1, arr2d_2, sep='\n\n')