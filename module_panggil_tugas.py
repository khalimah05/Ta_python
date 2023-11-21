# Memanggil Module
from tugas_module_lingkaran import lingkaran
from tugas_module_segitika import segitiga

# Output 
print("Pilih bangun ruang yang akan di hitung (1/2) ")
print("1.Lingkaran")
print("2.Segitiga")
print("-----------------------------------------------")
p =int(input("Pilih Bangun Ruang(1/2): "))
if p == 1 :
    print("Menghitung bangun Lingkaran")
    jari = int(input("Masukan jari jari lingkaran : "))
    hasil = lingkaran(jari)

else:
    print("Menghitung bangun segitiga")
    a = int(input("masukan nilai a : "))
    t = int(input("Masukan nilai t : "))
    s = int(input("masukan nilai sisi : "))
    hasil = segitiga(a,t,s)
