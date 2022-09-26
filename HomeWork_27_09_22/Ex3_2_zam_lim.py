# Ex3_2_zam_lim. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from os import sep
n = int(input("Введите число: "))
array_2_zam_lim = [0]*n
sum_num_array = 0
for i in range(1, n + 1):
    array_2_zam_lim[i - 1] = (1 + 1 / i ) ** i
    sum_num_array += array_2_zam_lim[i - 1]
print(array_2_zam_lim)
print(sum_num_array)