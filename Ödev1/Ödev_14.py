def ebob (sayı1,sayı2):
    liste=[]
    if(sayı1 > sayı2):
        for i in range(1,sayı1+1):
            if(sayı1%i == 0 and sayı2%i==0):
                liste.append(i)

    else:
        for i in range(1,sayı2+1):
            if(sayı1%i == 0 and sayı2%i==0):
                liste.append(i)
    liste.sort()
    print(liste)

    print("Ebobunuz {}".format(liste[-1]))

def ekok (sayı,sayı2):
    








sayı1 = int(input("Lütfen sayı değerini giriniz:"))
sayı2 = int(input("Lütfen sayı değerini giriniz:"))


print(ebob(sayı1,sayı2))



