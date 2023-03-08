#not,or,and,xor

#===NOT
a = True
b = not a
print("===NOT\n")
print(" Not ", a, " : ", b)


print("===OR\n")
a = True 
b = True
c = a or b
print(a, " OR ", b, ": ", c)

a = True 
b = False
c = a or b
print(a, " OR ", b, ": ", c)

a = False 
b = True
c = a or b
print(a, " OR ", b, ": ", c)

a = False
b = False
c = a or b
print(a, " OR ", b, ": ", c)

print("===AND\n")
a = True 
b = True
c = a and b
print(a, " AND ", b, ": ", c)

a = True 
b = False
c = a and b
print(a, " AND ", b, ": ", c)

a = False 
b = True
c = a and b
print(a, " AND ", b, ": ", c)

a = False
b = False
c = a and b
print(a, " AND ", b, ": ", c)

print("===XOR\n")
a = True 
b = True
c = a ^ b
print(a, " XOR ", b, ": ", c)

a = True 
b = False
c = a ^ b
print(a, " XOR ", b, ": ", c)

a = False 
b = True
c = a ^ b
print(a, " XOR ", b, ": ", c)

a = False
b = False
c = a ^ b
print(a, " XOR ", b, ": ", c)