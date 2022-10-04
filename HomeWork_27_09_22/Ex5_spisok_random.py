#  Написать программу перемешивающую список
import datetime
from random import randrange
from time import time
n = int(input('Введите количество элементов n = '))
array = [randrange(-99, 100) for i in range(n)]
print(array)
for i in range(len(array)):
    current = array[i]
    k = datetime.datetime.now().microsecond % n
    print(k)
    time.sleep(k*0.05)
    array[i] = array[k]
    array[k] = current 
print(array)




# def getRandomInt(randomRange):
#     return datetime.datetime.now().microsecond % randomRange


# def shuffleList(list):
#     shuffledLst = []
#     while (len(list) != 0):
#         index = getRandomInt(len(list))
#         el = list[index]
#         shuffledLst.append(el)
#         list.remove(el)
#     return shuffledLst
# import util

# baseLst = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(baseLst)
# shuffledLst = util.shuffleList(baseLst)
# print(baseLst)
# print(shuffledLst)

    

