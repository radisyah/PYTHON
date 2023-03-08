#Merubah dalam Upper Case
salam = "bro"
print("Normai = " + salam)
salam = salam.upper()
print("Upper = " + salam)

#Merubah semua dalam lower Casesalam = "bro"
salam = "BRO"
print("Normai = " + salam)
salam = salam.lower()
print("Upper = " + salam)

##Pengecekan dengan is Method

salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower " + str(apakah_lower))
apakah_lower = salam.isupper()
print(salam + " is upper " + str(apakah_lower))

#isalpha()<--- untuk mengecek semuanya huruf
#isalnum()<-- untuk huruf dan angka
#isdecimal()<-- Angka saja
#isspace()<-- spasi,tab, newline in
#istitle()<-- semua kata dimulai dengan huruf besar

judul = "star wars"
cek_judul = judul.istitle()
print(judul + " is title " + str(cek_judul))

#cek komponen startswith() endswith()

start = "star wars"
cek_start = start.startswith(("star"))
print(judul + " is start " + str(cek_start))

ends = "star wars"
cek_ends = ends.endswith(("wars"))
print(ends + " is ends " + str(cek_ends))

#penggabungan dan pemisahan join() split()

join = ("aku","sayang","kamu")
yok_join = " ".join(join)
print(yok_join)

yok_split = "aku benci dan sayang sama kamu"
print(yok_split.split("benci dan"))

#alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10,".")
print("+"+kanan+"+")

kiri = "kiri".ljust(10,".")
print("+"+kiri+"+")

center = "center".center(16,".")
print("+"+center+"+")

#kebalikanya strip()

center = center.strip(".")
print("+"+center+"+")




