matrislazim = []
matris = []
donme = 0
ana_depo = []
for i in range (2,21):
    for j in range(1,21):
        toplam = 0
        for rakamlar in str(i**j):
            toplam += int(rakamlar)
        matrislazim = [i,j,toplam]
        matris.append(matrislazim)


for o in matris:
    print(o)

while(donme < 380 ):
    ana_depo.append(matris[donme][2])
    donme += 1

print(max(ana_depo))
sayac = 0
while(sayac < 380 ):
    if (max(ana_depo)) == matris[sayac][2]:
        print(matris[sayac])
    sayac += 1









