tahun_lahir = int(input("Masukkan Tahu Lahir Anda"))
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir 
print(" umur anda", umur)

if umur < 18:
    print("anda belum bisa buat KTP")
else :
    print("anda sudah bisa buat KTP")