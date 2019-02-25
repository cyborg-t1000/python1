n = int(input('Number: '))


def left(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def right(n):
    return n * (n + 1) / 2


if left(n) == right(n):
    print('Равенство верно')
else:
    print('Равенство не верно')
