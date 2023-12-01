total = 0

while True :
    bilangan = int(input("massukan bilangan bulat positif"))

    if bilangan < 0:
        break
    total += bilangan
    
print("jumlah dari bilangan bilangan positif yang dimasukkan", total)
    