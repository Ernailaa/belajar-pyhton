print("selamat datang di Dafun")
nama=input("masukkan nama anda: ")
umur=input("masukkan umur anda: ")

print("halo" + nama + "selamat menikmati wahana DI Dafun")

harga = 0

daftar_wahana=["bianglala RP. 13.000","istana boneka RP. 10.000","rumah kaca RP. 15.000","roller coaster RP. 20.000"]
angka=1
for wahana in daftar_wahana :
    print(str(angka),".", wahana)
    angka= int(angka) +1
pilihan = input("masukkan pilihanmu :")
if pilihan == "1":
    print("tiket RP. 13.000 ")
    harga += 13000
elif pilihan == "2":
    print("tiket RP. 10.000")
    harga += 10000
elif pilihan == "3":
    print("tiket RP. 15.000")
    harga += 15000
elif pilihan == "4":
    print("tiket RP. 20.000")
    harga += 15000
else:
    print("pilih wahana yang ada di daftar")
pajak = int(2000)
total = (harga + pajak)
print("total harga")
print("total keseluruhan yang harus kamu bayar adalah , total")