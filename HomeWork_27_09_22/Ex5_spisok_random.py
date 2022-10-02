import datetime
from random import randrange
n = int(input('Введите количество элементов n = '))
array = [randrange(1, 10) for i in range(n)]
index = []*n
for i in range(n - 1):
    index[i] = datetime.datetime.now().microsecond % n
print(array)
for i in range(len(array)):
    current = array[i]
    array[i] = array[index[i]]
    array[index[i]] = current
print(array)

    

