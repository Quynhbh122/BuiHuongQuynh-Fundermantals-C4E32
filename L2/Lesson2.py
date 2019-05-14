# [IF CO BAN]

# age = 10
# if age <18:
#     print('baby') 

# [example]

# # age = 10
# # is_baby = age<10
# # print(is_baby)

# # num = 101
# # is_odd = num % 2 == 1
# # print(is_odd)

# # text = 'xin chao'
# # text_is_not_empty = len(text)>0
# # print(text_is_not_empty)

# age = 8
# is_baby = age<10

# if(is_baby):
#     print('baby')

# # [IF TRONG IF]

# so = input('nhap so')
# so = int (so)

# # if so>0:
# #     print('tri tuyet doi la:',so)
# # if so<0:
# #     print('tri tuyet doi la:', -so)

# # if so>0:
# #     print('tri tuyet doi la:',so)
# # else:
# #     print('tri tuyet doi la:', -so)

# if so>0:
#     print('tri tuyet doi la:',so)
# elif so<0:
#     print('tri tuyet doi la:', -so)
# else:
#     print('la so 0')

# [BLOCK]: thụt lề
# cùng cách lề/ cùng khối dòng

# age = int(input('age:'))

# # # 1 : else/elif chỉ nhận if của gần nhất; và phải có if trước đó

# # if age<13:
# #     print('baby')
# # elif age>18:
# #     print('adult')
# # else:
# #     print('teen')

# # # 2

# [IF IN IF] **************************************

# # if age>13:
# #     print('baby')
# #     if age<18:
# #     print('teen')
# #     else:
# #         print('adult')

# [FOR]: CẤU TRÚC LẶP

# for a in (0,3,'x'):
#     print('hi',a)

# for a in range(10):
#     if a % 2 == 1:
#         print(a)

# for k in range(10):
#     for v in range(k):
#         print(' ',v,end='')
#     print()

# [FOR IN FOR] **************************

# for k in range(10):
#     for v in range(10):
#         for x in range(10):
#             print(k,v,x)

# [RANG]: start, step, stop

# n = int(input('n=:'))

# tong = 0
# for v in range(n+1):
#     tong = tong + v
# print(tong)

# # [ngoài vòng for, i nhận giá trị cuối cùng của range]
# for i in range(10):
#     print(i)
# print(i)


# [NHỚ]

# PRINLIST , PRINT(*)