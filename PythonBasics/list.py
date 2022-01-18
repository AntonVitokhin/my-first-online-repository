from random import randint

a = int(input('Введите количество элементов в списке: '))
b = int(input('Введите количество списков: '))

m = [[randint(0, 100) for i in range(a)] for j in range(b)]
print(m)