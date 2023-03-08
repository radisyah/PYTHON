print("PROGRAM KONVERSI SUHU")
print("------------------")
print("1. Suhu dalam Celcius")
print("2. Suhu dalam Reamur")
print("3. Suhu dalam Farenheit")
print("4. Suhu dalam Kelvin")
print("------------------")
inp = int(input("Masukkan Angka: "))

if inp==1:
  celcius = float(input("Masukkan suhu dalam celcius: "))
  print("Suhu Celcius: ",celcius)
  #Reamur
  reamur = (4/5)*celcius
  print("Suhu Reamur: ",reamur)
  #Fahrenheit
  farenheit = ((9/5)*celcius)+32
  print("Suhu Farenheit: ",farenheit)
  #Kelvin
  kelvin = celcius + 273
  print("Suhu Kelvin: ",kelvin)
  print("\n-------------------\n")
elif inp==2:
  reamur = float(input("Masukkan suhu dalam Reamur: "))
  print("Suhu Reamur: ",reamur)

  #celcius
  celcius = (5/4)*reamur
  print("Suhu Celcius: ",celcius)
  #Fahrenheit
  farenheit = ((9/4)*reamur)+32
  print("Suhu Farenheit: ",farenheit)
  #Kelvin
  kelvin = ((5/4)*reamur) + 273
  print("Suhu Kelvin: ",kelvin)
  print("\n-------------------\n")
elif inp==3:
  farenheit = float(input("Masukkan suhu dalam Farenheit: "))
  print("Suhu Farenheit: ",farenheit)
  #celcius
  celcius = ((5/9)*farenheit)-32
  print("Suhu Celcius: ",celcius)
  #reamur
  reamur = ((4/9)*farenheit)-32
  print("Suhu Reamur: ",reamur)
  #Kelvin
  kelvin = (((5/9)*farenheit)-32)+273
  print("Suhu Kelvin: ",kelvin)
  print("\n-------------------\n")
elif inp==4:
  kelvin = float(input("Masukkan suhu dalam Kelvin: "))
  print("Suhu Kelvin: ",kelvin)

  #celcius
  celcius = (kelvin-273)
  print("Suhu Celcius: ",celcius)
  #reamur
  reamur =(4/5)*(kelvin-273)
  print("Suhu Farenheit: ",reamur)
  #Kelvin
  kelvin = ((9/5)*(kelvin-273))+32
  print("Suhu Kelvin: ",kelvin)
  print("\n-------------------\n")
else:
  print("Empty")

print("Terimakasih")