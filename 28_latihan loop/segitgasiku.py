from distutils.util import copydir_run_2to3


sisi = 9
count = 1
spasi = 4



# print("dengan for")
# for i in range(sisi):
#   print("*"*count)
#   count += 1

# print("dengan while")
# while True:
#   print("*"*count)
#   count += 1
#   if count > sisi:
#     break

print("Ganjil")
while True:
  
  if count % 2:
    print(" "*spasi+"*"*count)
    count += 1
    spasi-= 1
  else:
    count += 1
    continue
  
  if count > sisi:
    break


sisi_2  = 1
count_2 = 7
spasi_2 = 1


while True:

  if count_2 % 2:
    print(" "*spasi_2+"*"*count_2)
    count_2 -= 1
    spasi_2 += 1
  else:
    count_2 -= 1
    continue

  if count_2 < sisi_2 :
    break
    
  