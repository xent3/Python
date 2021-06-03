def fon(x,y):
    if(x > y):
        return True
    elif(y>x):
        return False
a=0
b=1
liste = []
liste1 = []


while True:
    i = (input("Değer giriniz:"))

    if (i == "q"):
        break


    liste.append(int(i))
print(liste)


for x in range(1,len(liste)+1):
    c = 1
    d = 2

    for u in range(1,len(liste)):
        if (liste[a:b]==liste[b:c]):
            c += 1
            d += 1
            continue
        if fon(liste[a:b],liste[c:d]):
            print("{} {}dan büyüktür".format(liste[a:b],liste[c:d]))
            c +=1
            d +=1
            liste1.append(liste[a:b])

        else:
            print("{} {}dan küçüktür".format(liste[a:b], liste[c:d]))
            c +=1
            d +=1
    a +=1
    b +=1

print(liste1)