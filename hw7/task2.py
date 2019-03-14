# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        l = array[:mid]
        r = array[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1


array = [random.uniform(0, 50) for i in range(10)]
print(array)
merge_sort(array)
print(array)
