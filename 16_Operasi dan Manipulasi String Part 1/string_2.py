nama_1 = 'UcUp'
nama_2 = 'D'
nama_3 = 'Fame'
nama_4 = 'Rahmat Dimas Syahputra'

#Menggabungkan String
nama_lengkap = nama_1 + " " +  nama_2 + "'" + nama_3
print(nama_lengkap)

#Menghitung panjang string
panjang = len(nama_lengkap)
panjang2 = nama_4.count("a")
print("Panjang String: " + str(panjang))
print("Panjang String: "+ str(panjang2))

#MencariString

d = "D"
status = d in nama_lengkap
print(d + " ada di string: " + str(status))

d = "D"
status = d not in nama_lengkap
print(d + " tak ada di string: " + str(status))

#mengalikanString

kali = "d" * 10
print(str(kali))
print("d"*10)

#mencariIndeks

print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-6 : " + nama_lengkap[6])
print("Index ke-(-1) : " + nama_lengkap[-1])
print("Index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-0:3 : " + nama_lengkap[0:4])
print("Index ke-3:8 : " + nama_lengkap[3:8])
print("Index ke-(0,2,4,8,10 : " + nama_lengkap[0:11:2])

#SizeString
size_min = min(nama_lengkap)
print("Paling Kecil: " + size_min)

size_max = max(nama_lengkap)
print("Paling Besar: " + size_max)

ascii_code = ord(" ")
print("ASCII code Spasi: " + str(ascii_code))

ascii_code2 = ord(",")
print("ASCII code koma: " + str(ascii_code2))

#JumlahhurufString
print("Jumlah huruf U di string: ", + nama_lengkap.count("U"))