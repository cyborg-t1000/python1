n = int(input('Количечество чисел: '))
c = int(input('Искомая цифра: '))
cnt = 0  # counter

for i in range(1, n + 1):
    num = int(input(f'Введи {i}-е число: '))

    while True:
        if num % 10 == c:
            cnt += 1
        num = int(num / 10)
        if num == 0:
            break

print(f'Цифра {c} встречается {cnt} раз')
