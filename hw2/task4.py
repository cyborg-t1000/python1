n = int(input('Number of elements: '))

result = 0
next = 1

while n > 0:
    result += next
    next /= -2
    n -= 1

print(f'sum: {result}')
