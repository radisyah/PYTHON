a = 5
b = 9

c = a | b

print("===OR")
print("a:",a,"biner:", format(a, "08b" ))
print("b:",b,"biner:", format(b, "08b" ))
print("           ",format(c, "08b" ))
print(a, "or", b, "   :",c)


c = a & b

print("\n===and")
print("a:",a,"biner:", format(a, "08b" ))
print("b:",b,"biner:", format(b, "08b" ))
print("           ",format(c, "08b" ))
print(a, "and", b, "  :",c)


c = a ^ b

print("\n===xor")
print("a:",a,"biner:", format(a, "08b" ))
print("b:",b,"biner:", format(b, "08b" ))
print("           ",format(c, "08b" ))
print(a, "xor", b, "  :",c)

c = ~b

print("\n===not")
print("b:",b,"biner:", format(b, "08b" ))
print("           ",format(c, "08b" ))
print("not", b, "    :",c)
d = 0b00001001
e = 0b11111111
print("Nilai: ", e^d, "biner: ", format(e^d,"08b"))

c = a >> 4

print("\n===>>")
print("a:",a,"biner:", format(a, "08b" ))
print("a:",a,"biner:", format(c, "08b" ))

c = a << 4

print("\n===<<")
print("a:",a,"biner:", format(a, "08b" ))
print("a:",a,"biner:", format(c, "08b" ))



