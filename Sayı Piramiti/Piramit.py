print("Merhabalar Programımıza Hoş Geldiniz")
a = 0
liste1 = []
liste2 = []
liste3 = []
liste4 = []
liste5 = []


while(a < 1 ):
    sira1 = str(input("Lütfen birinci satır için değer giriniz:"))
    liste1.append(sira1)
    a += 1
a = 0

while (a < 2 ):
    sira2 = str(input("Lütfen ikinci satır için değer giriniz:"))
    liste2.append(sira2)
    a += 1
a = 0

while(a < 3):
    sira3 = str(input("Lütfen üçüncü satır için değer giriniz:"))
    liste3.append(sira3)
    a += 1
a = 0
while(a < 4 ):
    sira4 = str(input("Lütfen dördüncü satır için değer giriniz:"))
    liste4.append(sira4)
    a += 1

a = 0
while(a < 5):
    sira5 = str(input("Lütfen beşinci satır için değer giriniz:"))
    liste5.append(sira5)
    a += 1


print("Piramitiniz...")
print(liste1)
print(liste2)
print(liste3)
print(liste4)
print(liste5)

print("-"*50)
print("Hadi Yolculuğumuza {} sayısı ile başlayalım...".format(liste1[0]))
print("-"*50)
print("Sonra {} sayısı ile devam edelim..".format(max(liste2)))
print("-"*50)
print("Daha Sonra {} sayısı ile devam edelim..".format(max(liste3)))
print("-"*50)
print("Daha Sonra {} sayısı ile devam edelim..".format(max(liste4)))
print("-"*50)
print("Ve En Son {} sayısı ile bitirelim..".format(max(liste5)))
print("-"*50)
print("Bize Destek Olmak İçin Abone Olup Harçlık Verebilirsiniz :D")




















