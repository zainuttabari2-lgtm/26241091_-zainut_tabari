#soal program identitas mahasiswa
nama = str(input("masukkan nama saya:"))
nim = int(input("masukkan nim saya:"))
prodi = str(input("masukkan prodi saya:"))
digit_nim = int(input("masukkan dua digit_trakhir:"))

print("============identitas saya===========")
print("nama saya :", nama)
print("nim saya :", nim)
print("prodi saya :", prodi)
print(" digit nim saya :",  digit_nim)

#menampilkan tipe data
print("Tipe Data Nama        :", type(nama))
print("Tipe Data NIM         :", type(nim))
print("Tipe Data Prodi       :", type(prodi))
print("Tipe Data 2 Digit NIM :", type(digit_nim))
print("=" * 34)