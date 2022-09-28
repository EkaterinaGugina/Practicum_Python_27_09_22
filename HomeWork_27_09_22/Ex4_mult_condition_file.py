# Ex4_mult_condition_file. Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
array_mult_num = [i for i in range(-n, n + 1)]
print(array_mult_num)
f = open('file.txt', 'r')
array_index = f.readline()
print(*f)
f.close
# mult_num_index = 1
# for i in array_index:
#     mult_num_index *= array_mult_num[int(i)]
    
    
    
#     n = int(input("Введите число: "))
# array_mult_num = [i for i in range(-n, n + 1)]
# print(array_mult_num)
# f = open('C:\Users\ЭкзаменСдам\Desktop\GeekBrains\Python\Practicum_Python_27_09_22\HomeWork_27_09_22/file.txt', 'r')
# array_index = (f.readline())
# print(array_index)
# f.close
# mult_num_index = 1
# for i in array_index:
#     mult_num_index *= array_mult_num[int(i)]