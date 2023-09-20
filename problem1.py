text = input('soz kiriting ')
harf = input('harif kiriting ')
count = 0
for i in range(len(text)):
    if text[i] == harf:
        count += 1
        if count == 2:
            print(i)
            break