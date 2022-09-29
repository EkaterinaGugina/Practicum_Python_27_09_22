# Ex2_array_mult_num_N. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) 

def factorial(k):
    if k == 1: return 1
    else:
        return k * factorial(k-1)
n = int(input('введите число n = '))
array = [factorial(i) for i in range(1, n+1)]
print(array)

# n = int(input("Введите число: "))
# array_mult_num = [0]*n
# array_mult_num[0] = 1
# for i in range(1, n):
#     array_mult_num[i] = array_mult_num[i - 1] * (i + 1)
# print(array_mult_num)
