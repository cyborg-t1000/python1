# задание 2-3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

import hw6.get_size


num = str(input('Введите целое число: '))
size = hw6.get_size.show_size(num)

result = ''
size += hw6.get_size.show_size(result)
for i in num:
    result = i + result
print(result)
size += hw6.get_size.show_size(i)

hw6.get_size.print_size(size)

# Total size is 79
