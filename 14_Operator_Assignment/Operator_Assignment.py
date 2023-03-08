a = 5


#Operasi Matematika
a += 5
print("Hasil += :",a)
a -= 1
print("Hasil -= :",a)
a /= 2
print("Hasil /= :",a)
a *= 4
print("Hasil *= :",a)

#Operasi modulu dan pangkat
a = 5

a %= 2
print("\nHasil %= :",a)
a **= 2
print("Hasil **= :",a)
a = 1928
a //= 3
print("Hasil //= :",a)


#Operasi Bitwiseb
a = True

print("\nTrue")

a &= True
print("Hasil &= :",a)
a |= False
print("Hasil |= :",a)

#Operasi Geser
a = 0b00110
print("Nilai a:", format(a,'04b'))

a >>= 2
print("Nilai a:", format(a,'04b') )
a <<= 5
print("Nilai a:", format(a,'04b') )
