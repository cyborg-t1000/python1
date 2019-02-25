import random

rnd = random.randint(0, 100)
attempts = 10

while attempts > 0:
    attempts -= 1
    num = int(input('Number: '))
    if rnd < num:
        print('Мое число меньше')
    elif rnd > num:
        print('Мое число больше')
    else:
        attempts = 0

if num == rnd:
    print('Вы угадали')
else:
    print(f'Попытки кончились, было загадано {rnd}')
