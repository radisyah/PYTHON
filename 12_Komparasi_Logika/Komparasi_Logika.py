#+++++++++5-------------10++++++++++
"""
inputUser = int(input("Masukkan Angka kurang dari 5\natau\nLebih dari 10\n: "))

#+++++++5---------
isKurangdari = (inputUser < 5)
print("\nKurang dari 5 :",isKurangdari)

#--------10+++++++
isLebihdari = (inputUser > 10)
print("\nLebih dari 10 :",isLebihdari)

#+++++++++5-------------10++++++++++
isCorrect = (isKurangdari or isLebihdari)
print("\nAngka yang anda masukkan:",isCorrect)

#---------5+++++++++10----------

inputUser = int(input("\nMasukkan Angka lebih dari 5\ndan\nkurang dari 10\n: "))

#--------5++++++++
isLebihdari = (inputUser > 5)
print("\nKurang dari 5 :",isLebihdari)

#++++++++10-------
isKurangdari = (inputUser < 10)
print("\nLebih dari 10 :",isKurangdari)

#---------0+++++++++10----------
isCorrect = (isKurangdari and isLebihdari)
print("\nAngka yang anda masukkan:",isCorrect)
"""

#TUGAS
print("-----0+++++5-----8+++++11------")
inputUser = int(input("Masukkan Angka kurang dari 5\natau\nLebih dari 11: "))


#------------0+++++++++++
isLebihdari = (inputUser>0)
print("lebih dari 0 :",isLebihdari)

#++++++++++++5-----------
isKurangdari = (inputUser<5)
print("kurang dari 5 :",isKurangdari)

isCorrect_1 = (isLebihdari and isKurangdari)
print("angka yang anda masukkan1:",isCorrect_1)


#------------8+++++++++++
isLebihdari_2 = (inputUser>8)
print("lebih dari 8 :",isLebihdari_2)

#++++++++++++11-----------
isKurangdari_2 = (inputUser<11)
print("kurang dari 11 :",isKurangdari_2)

isCorrect_2 = (isLebihdari_2 and isKurangdari_2)
print("Angka yang anda masukkan2:",isCorrect_2)

isfinal = (isCorrect_1 or isCorrect_2)

print("\nAngka yang anda masukkan FINAL:",isfinal)

print("\n++++0----5++++8----11++++")

inputUser = int(input("\nMasukkan Angka kurang dari 5\natau\nLebih dari 11: "))


#++++++0--------
isKurangdari = (inputUser<0)
print("kurang dari 0 :",isKurangdari)

#------5+++++++
isLebihdari = (inputUser>5)
print("lebih dari 5 :",isLebihdari)

isCorrect_1 = (isLebihdari or isKurangdari)

print("angka yang anda masukkan1:",isCorrect_1)


#++++++8--------
isKurangdari_2 = (inputUser<8)
print("kurang dari 8 :",isKurangdari_2)

#------11+++++++
isLebihdari_2 = (inputUser>11)
print("lebih dari 5 :",isLebihdari_2)

isCorrect_2 = (isLebihdari_2 or isKurangdari_2)

print("angka yang anda masukkan2:",isCorrect_2)


isfinal = (isCorrect_1 and isCorrect_2)

print("\nAngka yang anda masukkan FINAL:",isfinal)









