counter = 0
for i in range(32, 128):
    print(f'{i:3} {chr(i)}  ')  # todo: no EOL
    counter += 1
    if counter > 10:
        print('\n')
        counter = 0
