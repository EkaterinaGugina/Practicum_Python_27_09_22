# Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды
# t = 123456
# ss = t % 60
# mm = (t // 60) % 60
# hh = (t // 60) //60
# dd = ((t // 60) // 60) // 24
# print(f'{dd} дней {hh} : {mm} : {ss}')

sec = int(input(''))
min, sec = sec // 60, sec % 60
hour, min = min // 60, min % 60
day, hour = hour // 24, hour % 24
print(f"{day}:{hour}:{min}:{sec}")
