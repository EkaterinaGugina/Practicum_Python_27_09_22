# Ex4_mult_condition_file. Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
array_mult_num = [i for i in range(-n, n + 1)]
print(array_mult_num)
mult_num_index = 1
with open("file.txt", "r") as f:
    for line in f:
        mult_num_index *= array_mult_num[int(line)] 
print(mult_num_index)     # В file.txt записаны индексы 2, 1, 6
f.close


pos = int(input("Введите целое число больше 4: "))
addres = 'spisok.txt'

# Создание списка от -N до N
def Spisok (number):
    list = []
    for i in range(-number, number+1):
        list.append(i)
    return list

# # Создание списка из строки в файле
# def FileList(addresFile):
#     file = open(addresFile, 'r')
#     list = file.read()
#     file.close()
#     list = list.replace(" ", "")
#     list = list.split(",")
#     for i in range(len(list)):
#         list[i] = int(list[i])
#     return list

# list = Spisok(pos)
# sp = FileList(addres)
# print(list)
# print(sp)
# listX = 1
# for i in sp:
#     listX*=list[i]

# print(listX)
    
# # 2        ,4,     0,  10
# # 2,4,0,10
