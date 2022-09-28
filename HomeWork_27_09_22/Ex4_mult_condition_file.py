# Ex4_mult_condition_file. Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
array_mult_num = [i for i in range(-n, n + 1)]
print(array_mult_num)
mult_num_index = 1
with open("file.txt", "r") as f:
    for line in f:
        mult_num_index *= array_mult_num[int(line)]
print(mult_num_index)
f.close