while True:

    o = str(input('Operation: '))

    if o == '0':
        break

    a = int(input('First number: '))
    b = int(input('Second number: '))

    if o == '+':
        print(f'Result: {a+b}')
    elif o == '-':
        print(f'Result: {a-b}')
    elif o == '*':
        print(f'Result: {a*b}')
    elif o == '/':
        if b != 0:
            print(f'Result: {a/b}')
        else:
            print('Division by zero')
    else:
        print('Unknown operation')
