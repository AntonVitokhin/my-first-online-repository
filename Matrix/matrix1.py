import numpy as np
import random

n = int(input('Введите порядок матрицы: '))
choices = [-1, 1]

arr = np.array([[random.choice(choices) for i in range(n)] for j in range(n)])


def sum_matrix(matrix):
    result = 0
    for i in range(n):
        for j in range(n):
            result += (matrix[i, j] * matrix[i - 1, j]) + (matrix[i, j] * matrix[i, j - 1])
    return result


print(sum_matrix(arr))