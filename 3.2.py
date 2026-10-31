#Вариант 16
a = list(map(int, input("10 чисел через пробел: ").split()))

b = list()
for x in a:
    if x not in b:
        b.append(x)

print(*b)