#9 Напишите программу, которая выводит нечетные числа из заданного списка и останавливается, если встречает число 554.
lst = [23, 4, 67, -2, 5, 554, 765]
# lst = []
# for i in range(4):
#     num = int(input("Введите число: "))
#     lst.append(num)
for i in lst:
    num = int(i)
    if num % 2 != 0: print(i)
    elif i == 554:
        break