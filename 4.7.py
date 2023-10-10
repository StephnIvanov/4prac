n = int(input('Введите число n '))
z = 0
x = 1
for i in range(1, n + 1):
    x *= i
    z += x
print(z)