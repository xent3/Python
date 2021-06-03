def buyuk(x,y):
    if(x > y):
        return x
    else:
        return y
liste=[]
liste1=[]
a = 0
b = 1
d = 2
while True:
    i = (input("Değer giriniz:"))

    if (i == "q"):
        break


    liste.append(int(i))


uzunluk = int(len(liste))



for i in range(1,len(liste)):
    c = buyuk(liste[0], liste[i])
    c = buyuk(c, liste[i+1])
    d += 1
    print("============",d)
    print("uzuluk",uzunluk)
    print("d",d)
    print("c",c)


    print("liste",liste)
    print("liste1",liste1)
    liste.remove(c)
    liste1.append(c)

