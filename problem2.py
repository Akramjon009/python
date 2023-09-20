try:
    lis = list(input('son kiriting '))
    sets = list(set(lis))
    print(str(lis) - str(sets))
except TypeError:
    print('error')
    exec(1)
else:
    print('e')
