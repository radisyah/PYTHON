nama = "ucup"
umur = "17"
tinggi = "179"
prodi = "Akuntasi"

data_string = f"nama: {nama} \numur: {umur} \ntinggi: {tinggi} \nprodi: {prodi}"
print(data_string)


center = "Data Mahasiswa".center(24,"=")
print("\n"+center)

#string multiline
data_string = f"""nama  : {nama:>8} 
umur  : {umur:>8} 
tinggi: {tinggi:>8} 
prodi : {prodi:>8}
"""
print(data_string)
