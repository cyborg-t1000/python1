n = int(input('Number: '))

even = 0
odd = 0

if n == 0:
    even = 1
else:
    while n > 1:
        n = int(n)
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n / 10

print(f'Evens: {even}, odds: {odd}')
