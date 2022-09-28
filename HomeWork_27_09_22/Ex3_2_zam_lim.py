# Ex3_2_zam_lim. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

n = int(input("Введите число: "))
sum_num_array = 0
for i in range(1, n + 1):
    sum_num_array += (1 + 1 / i ) ** i
print(f'Для n = {n}: сумма = {round(sum_num_array, 2)}')



# n = int(input("Введите число: "))
# array_2_zam_lim = [0]*n
# sum_num_array = 0
# for i in range(1, n + 1):
#     array_2_zam_lim[i - 1] = (1 + 1 / i ) ** i
#     sum_num_array += array_2_zam_lim[i - 1]
# print(array_2_zam_lim)
# print(f'Для n = {n}: сумма = {sum_num_array}')

