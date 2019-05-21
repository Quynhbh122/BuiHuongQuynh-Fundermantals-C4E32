def get_even_list(l):
    ds = []
    for i in range(len(l)):
        if l[i]%2 == 0:
            ds.append(l[i])
        
    print(ds)
    return ds

a = [1,4,5,-1,10]
get_even_list(a)

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
