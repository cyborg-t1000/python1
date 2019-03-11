import sys


def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                size +=  show_size(item)
    return size


def print_size(x):
    print(f'\nTotal size is {x}')
