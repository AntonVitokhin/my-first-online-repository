import random

print('Добро пожаловать в игру "камень, ножницы, бумага"')

a = ['rock', 'paper', 'scissors']
my = 0

while True:
    while my not in a:
        my = input('Введи один из вариантов (rock, paper или scissors): ')

    machine = random.choice(a)
    print(machine)

    if machine == my:
        print('В этот раз ничья')
    elif (my == 'rock' and machine == 'scissors') or (my == 'paper' and machine == 'rock') or (
            my == 'scissors' and machine == 'paper'):
        print('Вы победили. Так держать!')
    else:
        print('Вы проиграли. Повезёт в следующий раз')

    if input('Сыграем ещё раз? ').lower() in 'yes':
        my = 0
    else:
        print('До встречи!')
        break


