# # -------------------------------------------- [FUNCTION]-------------------------------------------------------------

# a = []
# n = int(input('so phan tu cua day so: '))
# for i in range (n):
#     so = float(input('moi ban nhap so: '))
#     a.append(so)

# tong = 0
# for b in a:
#     tong = tong + b

# print('tong day so vua nhap la: ', tong)

# print('trung binh day so vua nhap la: ', tong/n)

# # ----------------------------------------------- [CÓ THAM SỐ, KHÔNG RETURN] -----------------------------------------------------------
# def add_two_number(a,b):
# #     a = int(input('nhap so thu nhat: '))
# #     b = int(input('nhap so thu hai: '))
#     print('tong hai so la: ', a+b )
#     return a+b

# a=1
# b=2
# x=5
# y=7

# add_two_number(x,y)

# tong1 = add_two_number(a,b)
# tong2 = add_two_number(tong1,c)

# # ----------------------------------------------- [CÓ THAM SỐ, CÓ RETURN] -----------------------------------------------------------------
# def abs_of_number(a):
#     if a>0:
#         return a
#         print('tri tuyet doi la: ',a)
#     else:
#         return -a
#         print('tri tuyet doi la: ',-a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)

# # ------------------------------------------------- [EX] ----------------------------------------------------
# def evaluate(a,b,c):
#     if c == '+':
#         print('tong cua 2 so la:', a+b)
#         return a+b
#     if c == '-':
#         print('hieu cua 2 so la:',a-b)
#         return a-b
#     if c == '*':
#         print('tich cua 2 so la:', a*b)
#         return a*b
#     if c == '/':
#         print('thuong cuar 2 so la:', a/b)
#         return a/b

# evaluate(4,0,'+')

# def eval_expression(s):
#     a = int(s[0])
#     b = int(s[2])
#     o = s[1]
#     return evaluate(a,b,o)

# while True:
#     s = input('nhap bieu thuc: ')
#     print('gia tri bieu thuc vua nhap la:', eval_expression)

# ----------------------------------------------------------- [EX 2] -------------------------------------------------------------------
n = 9
def la_so_nguyen_to(n):
    for v in range(2,n):
        if n % v ==0:
            return False
    return True

so_ngto = []
for k in range (2, 10000):
    if la_so_nguyen_to(k):
        so_ngto.append(k)

print(so_ngto)
len(so_ngto)

