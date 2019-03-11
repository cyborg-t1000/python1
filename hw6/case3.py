# задание 2-3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

import hw6.get_size


num = str(input('Введите целое число: '))
size = hw6.get_size.show_size(num)

result = num[::-1]
size = hw6.get_size.show_size(result)

print(result)

hw6.get_size.print_size(size)

# Total size is 28
