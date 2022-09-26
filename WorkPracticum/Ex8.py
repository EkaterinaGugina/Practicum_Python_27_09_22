# №8 Написать программу проверки, является ли строка палиндромом
# n = 'abba'
# count = 0
# for i in range(len(n)//2):
#     if n[i]==n[-1-i]:
#         count+=1
# if count==(len(n)//2):
#     print('Полидром')
# else:
#     print('не полидром')

# Другой способ полиндрома в одну строку

string = 'лешанаполкеклопанашел'
rev_string = string[::-1]
if string == rev_string:
    print('это полиндром')
else:
    print('не полиндром')