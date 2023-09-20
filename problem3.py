num = str()
while True:
        n = input('son kiriting ')
        if n != 'c':
            num += n
        else:
            break
print(sum(num))