print(20*"=")
print("Kalkulator Sederhana")
print(20*"="+"\n")

angka_1 = float(input("Masukkan Angka 1: "))
operator = input("(+,-,x,/): ")
angka_2 = float(input("Masukkan Angka 2: "))

if operator == "+":
  hasil = angka_1 + angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")
elif operator == "-":
  hasil = angka_1 - angka_1
  print(f"{angka_1} - {angka_2} = {hasil}")
elif operator == "x" or operator == "*":
  hasil = angka_1 * angka_2
  print(f"{angka_1} x {angka_2} = {hasil}")
elif operator == "/":
  hasil = angka_1 / angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")
else:
  print("404 Not Found")

print("\n"+20*"=")
print("Terimakasih")








