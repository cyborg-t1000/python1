counter = 0
for i in range(32, 128):
    print(f'{i:3}-{chr(i)}  ', end='')
    counter += 1
    if counter >= 10:
        print('')
        counter = 0
