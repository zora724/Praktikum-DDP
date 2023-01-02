from Harimau import *
from lumbaLumba import *
from Elang import *

# Objek dari class animal
Harimau = Harimau("Harimau", "Daging", "Darat","Beranak", "Hutan", "Mamalia")
lumba_lumba= lumba_lumba("Lumba-lumba", "Ikan, Cumi-cumi dan Krustasea", "Air","Beranak", "Laut dan Sungai", "Mamalia")
Elang = Elang("Elang", "Tikus", "Udara","Bertelur", "Hutan", "Unggas")

# Cetak properti dan method Harimau
print("======================================")
print("Nama Hewan =", Harimau.nama)
print("Makanan =", Harimau.makanan)
print("Hidup =", Harimau.hidup)
print("Berkembang Biak =", Harimau.berkembangBiak)
Harimau.display_habitat()
Harimau.display_jenis()

# Cetak Properti & Method Lumba-lumba
print("======================================")
print("Nama Hewan =", lumba_lumba.nama)
print("Makanan =", lumba_lumba.makanan)
print("Hidup =", lumba_lumba.hidup)
print("Berkembang Biak =", lumba_lumba.berkembangBiak)
lumba_lumba.display_habitat()
lumba_lumba.display_jenis()

# Cetak properti & method Elang
print("======================================")
print("Nama Hewan =", Elang.nama)
print("Makanan =", Elang.makanan)
print("Hidup =", Elang.hidup)
print("Berkembang Biak =", Elang.berkembangBiak)
Elang.display_habitat()
Elang.display_jenis()
