#Format String
string = "hello"
format_string = f"hello {string}"
print(format_string)

#Format Boolean
Boolean = False
format_string = f"Boolean = {Boolean}"
print(format_string)

#format pecahan
angka = 25.34343434
format_string = f"Pecahan = {angka:.2f}"
print(format_string)

#Format bilangan bulat
angka = 25
format_string = f"Bulat = {angka}"
print(format_string)

#format jutaan
angka = 25000000
format_string = f"Jutaan = {angka:,}"
print(format_string)

#Format Leading Zero
angka = 234
format_string = f"Leading zero = {angka:010.2f}"
print(format_string)

#Format minus dan positif
angka = 24
format_string = f"positif = {angka:+d}"
print(format_string)

angka = -24
format_string = f"negatif = {angka:+d}"
print(format_string)

#format persen
angka = 0.012123
format_string = f"persen = {angka:.2%}"
print(format_string)

#format perhitungan
biaya1 = 10
biaya2 = 500
format_string = f"Harga = Rp. {biaya1*biaya2:,}"
print(format_string)

#format sistem bilangan
angka = 123
format_bin = f"bin =  {bin(angka)}"
format_oc = f"oc =  {oct(angka)}"
format_hex = f"hex =  {hex(angka)}"

print(format_bin)
print(format_oc)
print(format_hex)
