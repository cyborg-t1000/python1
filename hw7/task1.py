# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        flag = True  # были ли перестановки за проход
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = False
        if flag:
            break
        n += 1


array = [i for i in range(-100, 101)]
random.shuffle(array)
print(array)
bubble_sort(array)
print(array)
