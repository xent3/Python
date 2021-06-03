import time
print("****************************************")
print("Herkese Merhabalar Bu Sunumda Size Neden Efe'ye oyundan istediği bir şeyi almanız gerektiğini açıklayıp size yardımcı olacağım.")
print("----------------------------------------")
ad = input("Adınızı alabilir miyim lütfen:")
soyad = input("Soyadınızı da baheşedebilir misiniz:")
print("Kart bilgilerinizi de alabilir miyim acaba:")
time.sleep(1)
print("Şaka yaptım şaka hadi devam edelim")
print("----------------------------------------")

print("İlk olarak sebepleri saymakla başlayabilirim sanırım")
time.sleep(1)
hak = 3

print("----------------------------------------")
print("Menümüze Hoşgeliniz lütfen hangi sebebi istediğinizi seçiniz...")
time.sleep(1)
print("----------------------------------------")
print("1.Sebep")
print("2.Sebep")
print("3.Sebep")
while hak > 0:
    sebep = int(input("Sebebi seçiniz lütfen(3 hakkınız var:"))

    if(sebep == 1):
        print("Kitap başına 100 tl hakkını kullanmak istemesi")
        print("(✿◠‿◠)")
        hak-=1
    elif(sebep == 2):
        print("Uzun zamandır oyun almaması")
        print("(✿◠‿◠)")
        hak-=1
    elif(sebep== 3):
        print("Çok uslu bir çocuk olması")
        print("(✿◠‿◠)")
        hak -=1

    else:
        print("öyle bir hakkın yok")
        continue
print("----------------------------------------")
print("Sebeplerimize baktığımıza göre herhalde Efe'nin hak ettiği konusunda hemfikir olmuşuzdur.")
print("Hadi o zaman Nasıl bu işin altından kalkabileceğimize bakalım.")


time.sleep(2)



hak1 =2
while hak1 > 0:
    print("Seçenekleri seçiniz...")

    print("1-Oyuna yatırmasına izin vermemek")
    print("2.İzin vermek ")

    secim =int(input("Seçiminiz Hangisidir:"))

    if(secim ==1):
        print("----------------------------------------")
        print("Hadi ama dostum bir daha düşünebilirsin sanki ne dersin?")
        print("----------------------------------------")
        hak1 -=1
    elif(secim ==2):
        print("----------------------------------------")
        print("Aferim sen de artık bizim dilden konuşmaya başlıyorsun")
        print("----------------------------------------")
        hak1-=1

print("Şimdi senin için yapabileceklerime bir bakayım...")
time.sleep(1)

print("Hadi gene iyisin seç")
print("1-Para yardımı")
print("2-Yazılımsal yardım")

hak2=2
while hak2 > 0:
    secim2 =int(input("Seçiminiz Hangisidir:"))

    if(secim2 ==1):
        print("Al 70 tl hayırlı olsun")
        hak2 -=1
    elif(secim2 ==2):
        print("Bekle bakem geliyom")
        hak2-=1
time.sleep(2)
print("----------------------------------------")


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