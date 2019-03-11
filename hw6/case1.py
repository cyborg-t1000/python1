# задание 2-3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

import hw6.get_size

num = int(input('Number: '))
size = hw6.get_size.show_size(num)

while True:
    print(num % 10, end='')
    num = int(num / 10)
    if num == 0:
        break

hw6.get_size.print_size(size)

# Total size is 14

# Лучший вариант - используется меньше всего памяти, но исходная переенная не сохраняется
