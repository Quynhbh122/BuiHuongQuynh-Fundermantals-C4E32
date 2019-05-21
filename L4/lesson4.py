# [dictionary]-------------------------------------------------------------------------------------------------------
persons = [
{'ten': 'Bui Linh Chi', 'v1': 82, 'v2': 63, 'v3': 86},
{'ten': 'Nguyen Hoai Thuong', 'v1': 82, 'v2': 60, 'v3': 80},
{'ten': 'Tran Thi Huong Lien', 'v1': 74, 'v2': 63, 'v3': 94}]

# print(person[2]['ten'])
# v1 = person[2]
# ten = v1['ten']
# print(v1['ten'])


# # [ex]: tạo từ điển --------------------------------------------------------------------------------------------------

# dic = {'mouse': 'con chuot', 'keyboard': 'ban phim', 'monitor': 'man hinh'}
# while True:
#     tu = input('nhap tu can tra: ')

#     if tu in dic:
#         print(dic[tu])
#         break
#     elif len(tu)==0:
#         break
#     else:    
#         print('tu ban can tim se duoc cap nhat som nhat')
    
# # [for v in dict] 
# for v in dic:
#     print(v)

# [them key vao 1 mang]=================================================================================================
v2 = int(input('nhap so do vong 1: '))
for p in persons:
    if v2 == p['v2']:
        print(p['ten'])
