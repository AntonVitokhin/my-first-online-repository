import matplotlib.pyplot as plt
import numpy as np
import random

n = int(input('Введите порядок матрицы: '))
repeat = int(input('Введите количество итераций: '))
T = float(input('Введите значение переменной Т: '))
choices = [-1, 1]


def sum_matrix(matrix):  # Функция, которая выводит сумму элементов матрицы
    result = 0
    for i in range(n):
        for j in range(n):
            result += (matrix[i, j] * matrix[i - 1, j]) + (matrix[i, j] * matrix[i, j - 1])
    return result


arr = np.array([[random.choice(choices) for i in range(n)] for j in range(n)])  # Создание матрицы

for k in range(repeat):
    E1 = sum_matrix(arr)

    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    arr[a][b] *= -1  # Замена случайного числа матрицы на противоположное по знаку

    E2 = sum_matrix(arr)
    delta = E2 - E1

    if delta <= 0:  # Если delta >= 0, то принимаем новую конфигурацию
        continue
    else:  # Иначе вычисляем «вероятность перехода»
        W = np.exp(-delta / T)
        P = random.random()

        if P <= W:  # Если P <= W, то принимаем новую конфигурацию
            continue
        else:  # Иначе возвращаем старую конфигурацию
            arr[a][b] *= -1

fig, ax = plt.subplots()

ax.imshow(arr)

fig.set_figwidth(n)
fig.set_figheight(n)

plt.show()