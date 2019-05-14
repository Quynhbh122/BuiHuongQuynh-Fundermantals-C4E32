sizes = [5,7,300,90,24,50,75]
print ('Hello, my name Quy and these are my sheep sizes:')
print (*sizes, sep = ", ")
print ('now my biggest sheep has size ', max(sizes), ", let'shear it")
sizes.remove(max(sizes))
print ('After shearing, here is my flock:')
print (*sizes, sep = ", ")

for a in range (4):
    print('month ', a+1)
    for i in range(len(sizes)):
        sizes[i] = sizes[i] + 50
    print ('One month has passed, now here is my fock:')
    print(sizes)

b = sum(sizes)
print('My flock has sizes total: ', b)
print('I would get ', b , "*2$", " = ", b*2 , "$")