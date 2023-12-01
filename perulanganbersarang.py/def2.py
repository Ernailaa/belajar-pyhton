def hitung(angka1, angka2, operator) :
     if(operator == "+"):
         return angka1 + angka2
     elif(operator == "-"):
         return angka1 - angka2
     elif(operator == "x"):
         return angka1 * angka2
     else:
         print("masukan dengan benar")
print(hitung(5,3, "+"))
print(hitung(5,3, "-"))
print(hitung(5,3, "x"))

# def perulangan(nama, perulangan):
#     for i in range(perulangan):
#         print(nama)
# perulangan(" can i call you my everything call you my baby ", 10)
