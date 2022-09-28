# match subject:
    # case <pattern_1>:
    #     <action_1>
    # case <pattern_2>:
    #     <action_2>
    # case <pattern_3>:
    #     <action_3>
    # case _:
    #     <action_wildcard>
    
# q = int(input('Input number of Quoter :'))

# match q:
#     case 1:
#         print(' X > 0 and Y > 0')
#     case 2:
#         print(' X < 0 and Y > 0')
#     case 3:
#         print(' X < 0 and Y < 0')
#     case 4:
#         print(' X > 0 and Y < 0')
#     case _:
#         print('Uncorrect number')



# Ex_1 Посчитайте, сколько раз символ встречается в строке.
string = "Посчитайте, сколько раз символ встречается в строке."
res = 0
simb = input('Введите символ: ')
for i in string:
    if i == simb:
        res+=1
print(f'символ {simb} встретился в этой строке {res} раз')
