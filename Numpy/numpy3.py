import numpy as np

arr1 = np.random.randint(-100, 100, 50)
arr2 = arr1[::-1]
print(arr1, arr2, sep='\n\n')