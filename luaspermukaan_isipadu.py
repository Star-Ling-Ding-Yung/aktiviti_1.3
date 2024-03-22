#Atur cara mengira jumlah luas permukaan dan isipadu silinder
#Isytihar pemalar
pi=3.142

#Input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

#Proses
jumlah_luas_permukaan=(2*pi*jejari*jejari)+(2*pi*jejari*tinggi)
isipadu=pi*jejari*jejari*tinggi

#Output
print("Jumlah luas permukaan silinder ialah",round(jumlah_luas_permukaan,2))
print("Isi padu silinder ialah",round(isipadu,2))
