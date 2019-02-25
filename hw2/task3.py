n = int(input('Number: '))

while True:
    print(n % 10)  # todo: print without EOL
    n = int(n / 10)
    if n == 0:
        break

