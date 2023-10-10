a = int(input('Введите число '))
b = int(input('Введите второе '))
while a != b:
    print(a)
    if a < b:
        a += 1
    elif b < a:
        a -= 1
print(b)