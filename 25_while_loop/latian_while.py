print(20*"=")
print("Kalkulator Sederhana")
print(20*"="+"\n")

angka_1 = float(input("Masukkan Angka 1: "))
operator = input("(+,-,x,/): ")
angka_2 = float(input("Masukkan Angka 2: "))

while True:
  if operator == "+":
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
  elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"{angka_1} - {angka_2} = {hasil}")
  elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"{angka_1} x {angka_2} = {hasil}")
  elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"{angka_1} / {angka_2} = {hasil}")
  else:
    break
  operator = input("(+,-,x,/): ")
  angka_3 = float(input("Masukkan Angka: "))
  angka_2 = angka_3
  angka_1 = hasil
  
print("\n"+20*"=")
print("Terimakasih")








