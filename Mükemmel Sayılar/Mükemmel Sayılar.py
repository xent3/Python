
j = 1
liste = []
toplam = 0

for i in range(1,29):
    if(i == 1):
        continue
    for j in range(1,(i//2)+1):
            if( i % j == 0):
                print ("Tam Bolen:",j)
                liste.append(j)
                print("Liste", liste)
                for eleman in liste:
                    toplam += eleman
print("Toplam:",toplam)
liste = []


    if(toplam == i ):
        print ("Sayınız:",i,"Mükemmel Sayıdır Like Me!!!!")
        liste = []
        toplam = 0
    else:
        liste = []
        toplam = 0









