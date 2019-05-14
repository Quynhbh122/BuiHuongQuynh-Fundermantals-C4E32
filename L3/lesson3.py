# while True:
#     print('hi')

# # ctr+c dừng cái đang chạy

# # while không biết trước số lần lặp, cần điều kiện để dừng; kiểm tra điều kiện trước làm sau

# while False:
#     print ('hi')

# [THAY WHILE CHO FOR]

# dem = 0
# while True:
#     print ('hi',dem)
#     dem += 1 # dem = dem + 1
#     if dem>=10:
#         break
# print('end')

# [ĐẶT BIẾN TRUE/FALSE ĐỂ THOÁT CHỈ KHI HẾT VÒNG]

# mk = input('Vui long nhap mat khau')
# while len(mk) > 8:
#     mk = input('Mat khau chua nhieu nhat 8 ky tu, moi ban nhap lai mat khau khac')
# print('Da cap nhat mat khau thanh cong')

# while True:
#     pw = input('nhap pass:')
#     if len(pw)<8:
#         break

# [BÀI TẬP LÃI SUẤT]

# n = 0
# i = 0.65
# m = 21000000
# for n in range(10):
#     n += 1
#     m = m + m*i
# print ('sau 9 nam, so tien trong tai khoan la:', m)
# while m>=1200000000:
#     print ('so nam can de du tien mua nha la:', n)
#     break

# [LIST] = 1 LOẠI [CẤU TRÚC DỮ LIỆU]

# [CẤU TRÚC DỮ LIỆU] + [THUẬT TOÁN] = [CHƯƠNG TRÌNH]

# x=1
# y=x
# x=2
# print(y) # 1

#append thêm vào cuối/ insert thêm vào vị trí chọn (vị trí âm đi từ dưới lên)

#update không thay đổi số phần tử

#del => chỉ trên 1 dòng

n = int(input ('nhap so phan tu:'))
ds =[]
for i in range(n):
    so = input('nhap so thu ' + str(i) + ':')
    ds.append(int(so))
x
print('day so vua nhap la:')
print(ds)


# so_phan_tu_chan = 0
# tong_so_chan = 0
# for v in ds:
#     if v %2 == 0:
#         print(v)
#         tong_so_chan = tong_so_chan + v
#         so_phan_tu_chan += 1

# print('trung binh con cac phan tu chan la:',tong_so_chan/so_phan_tu_chan)

# ds_chan = []
# for v in ds:
#     if v % 2 ==0:
#         ds_chan.append(v)

# print('cac phan tu chan la:',ds_chan)
# print('tbc laf:',sum(ds_chan/len(ds_chan)))

ds_chan = [x for x in ds if x % 2 == 0]