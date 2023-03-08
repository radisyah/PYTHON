from msilib import Binary


x = 13
y = 6

print("nilai x: ",x,"id: ", hex(id(x)))
print("nilai y: ",y,"id: ", hex(id(y)))
hasil = x is not y
print("x is not y", hasil)

x = 5
y = 5

print("\nnilai x: ",x,"id: ", hex(id(x)))
print("nilai y: ",y,"id: ", hex(id(y)))
hasil = x is not y
print("x is not y", hasil)

x = 5
y = 5

print("\nnilai x: ",x,"id: ", hex(id(x)))
print("nilai y: ",y,"id: ", hex(id(y)))
hasil = x is  y
print("x is y", hasil)

x = 5
y = 6

print("\nnilai x: ",x,"id: ", hex(id(x)))
print("nilai y: ",y,"id: ", hex(id(y)))
hasil = x is y
print("x is not y", hasil)