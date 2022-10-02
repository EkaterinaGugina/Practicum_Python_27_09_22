#  Написать программу перемешивающую список
from cmath import exp
import datetime
from random import randrange
n = int(input('Введите количество элементов n = '))
array = [randrange(-99, 100) for i in range(n)]
print(array)
for i in range(len(array)):
    current = array[i]
    k = datetime.datetime.now().microsecond % n
    # print(k)
    array[i] = array[k]
    array[k] = current 
print(array)

    

