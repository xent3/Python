sayac = 0
liste = []
toplam = 0

for i in range(2,100):
    sayac = 0
    for j in range(1,(i+1)):
        if(i % j ==  0):
            sayac += 1

    if(sayac > 2 ):
        continue


    else:
        liste.append(i)

print(liste)


for a in liste:
    toplam += a

print("Toplamları:",toplam)









