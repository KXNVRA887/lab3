#Вариант 1
p = ("Ели еду, ель и осина, егерь ест ежа")
count = 0
for word in p.lower().split():
    if word.startswith("е"):
        count += 1

print("Слов на «е»:", count)