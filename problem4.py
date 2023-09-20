with open('txt.txt', 'r') as h:
     n = h.read().split(' ')
print(n)
for i in n:
    if 'a' in str(n).lower():
        with open('a.txt', 'a') as a:
            a.write(i + ' ')
    if 'k' in str(n).lower():
        with open('k.txt', 'a') as k:
            k.write(i + ' ')