#Вариант 16
a = list(map(int, input("Числа через пробел: ").split()))

prev = None
for x in a:
    if prev is not None and prev >= 0 and x >= 0:
        print(prev, x)
    prev = x