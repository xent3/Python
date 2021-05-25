print(""" ----Programımıza Hoş Geldiniz !!!!!!
Lütfen Bize Destek Olmak İçin Harçlık Veriniz----""")
print("-"*44)


sayı = int(input("Lütfen bir sayı giriniz:"))
basamak = len(str(sayı))
a = 0
toplam = 0
liste=[]
toplam1 = 0



while( basamak < int(len(str(sayı))) ):
    basamak += 1
print("Basamak sayısı... : {}".format(basamak))








for i in (range(0,basamak)):
    toplam = int(str(sayı)[a]) ** 3
    a+= 1
    liste.append(toplam)


for eleman in liste:
    print(eleman)
    toplam1 += eleman
    print("Toplam",toplam1)




if(toplam1 == sayı):
    print("Sayınız Armstrong Sayısıdır:",sayı)
else:
    print("Sayınız Armstrong Sayısı Değildir:",sayı)
