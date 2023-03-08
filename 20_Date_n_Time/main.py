import datetime as dt

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun")