# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Блок-схемы тут: https://drive.google.com/file/d/1RgRCoicYjOREaWbwNvwSh9nkf3rDpnuI/view?usp=sharing

x = int(input('Введите трехзначное число: '))
x = str(x)
print(f'Суммма: {int(x[0]) + int(x[1]) + int(x[2])}')
print(f'Произведение: {int(x[0]) * int(x[1]) * int(x[2])}')
