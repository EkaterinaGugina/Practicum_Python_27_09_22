# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#  Пример:
# Для N = 5: 1, -3, 9, -27, 81
from tkinter import N


n = int(input("Введите число: "))
# lst = [0]*n
# lst[0] = 1
# for i in range(1, n):
#     lst[i] = lst[i - 1]*(-3)
    
# for i in range(5):
#     print((-3) ** i, end=" ")

number = int(input("Введите число: "))
num = 1
for i in range(number):
    print(num, end=" ")
    num *= -3
