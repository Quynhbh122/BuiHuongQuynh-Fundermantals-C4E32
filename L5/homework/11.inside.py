# def is_inside( [x1,y1] , [x2,y2,width,height] ):
#     if x1 in range (x2, x2 + width + 1 )\
#     and y1 in range (y2, y2 + height + 1 ):
#         return True
#     else:
#         return False

# if is_inside([10,2],[1,1,20,20]):
#     print('Diem nam trong hinh')
# else:
#     print('Diem nam ngoai hinh')    

def is_inside(point,rec):
    if point[0] in range(rec[0],rec[0]+rec[2]+1) \
    and point[1] in range(rec[1],rec[1]+rec[3]+1):
        return True
    else:
        return False
    
point_coor = [10,2]
rec_coor = [1,1,20,20]
is_inside(point_coor,rec_coor)
if is_inside:
    print('Diem nam trong hinh')
else:
    print('Diem nam ngoai hinh')