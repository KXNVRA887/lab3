#Вариант 16
people = 0
area = 0

for i in range(12):
    people += float(input("Жители (тыс.): "))
    area += float(input("Площадь (км2): "))

print("Плотность:", people * 1000 / area, "чел./км2")