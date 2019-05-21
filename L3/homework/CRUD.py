
#R
print('welcome to our shop, what do you want?')
inventories = ['T-shirt','Sweater']
print('R')
print(*inventories, sep = " or ")

#C
inventories.append('Jean')
print('C')
print(*inventories, sep = " or ")

#U
inventories.insert(1,'Skirt')
inventories.pop(3)
print('U')
print(*inventories, sep = " or ")

#D
del inventories[2]
print('D')
print(*inventories, sep = " or ")