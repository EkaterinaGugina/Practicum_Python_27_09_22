# Найти максимальное из пяти чисел
# lst = [1, 3, 5, -1, 22]
lst = []
for i in range(5):
    num = int(input("Введите число: "))
    lst.append(num)

res = lst[0]
for i in range(1, 5):
    if lst[i] > res:
        res = lst[i]
print(res)