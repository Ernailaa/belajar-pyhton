#print("pertambahan")
#for i in range(1, 6) :
#    print(i)
#    for j in range(1, 6) :
#        print(i, "+", j, "=", int(i+j))

kumpulanBarang = [ ["meja", 'kursi', "tatakan"], ["monitor", "TV", "handphone"]]
for barang in kumpulanBarang :
    for item in barang :
        print(item, end=",")
    print()