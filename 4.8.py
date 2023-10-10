n = int(input("Введите число n (n меньше или равно 9): "))
for i in range(1, n + 1):
    for z in range(1, i + 1):
        print(z, end="")
    print()