x1 = int(input("1.nokta için x değerini giriniz:"))
y1 = int(input("1.nokta için y değerini giriniz :"))
x2 = int(input("2.nokta için x değerini giriniz :"))
y2 = int(input("2.nokta için y değerini giriniz :"))

ToplamX = x1 - x2
ToplamY = y1 - y2
Hipotenüs = ToplamX**2 + ToplamY **2

if (x1 > 0 and y1 > 0 ):
    print("Birinci Noktanız Birinci Bölgededir")
elif (x1 > 0 and y1 < 0):
    print("Birinci Noktanız Dördüncü Bölgededir")
elif (x1 < 0 and y1 > 0 ):
    print("Birinci Noktanız İkinci Bölgededir")
elif (x1 < 0 and y1 < 0 ):
    print("Birinci Noktanız Üçüncü Bölgededir")

if (x2 > 0 and y2 > 0 ):
    print("İkinciNoktanız Birinci Bölgededir")
elif (x2 > 0 and y2 < 0):
    print("İkinci Noktanız Dördüncü Bölgededir")
elif (x2 < 0 and y2 > 0 ):
    print("İkinci Noktanız İkinci Bölgededir")
elif (x2 < 0 and y2 < 0 ):
    print("İkinci Noktanız Üçüncü Bölgededir")

if(x1 == 0 and y1 > 0 ):
    print("Birinci Noktanız Y Ekseni Üstündedir")
elif(x1 == 0 and y1 < 0 ):
    print("Birinci Noktanız Y Ekseni Üstündedir")
elif(x1 == 0 and y1 == 0 ):
    print("Birinci Noktanız Orjindedir")
elif (x2 == 0 and y2 == 0):
    print("İkinci Noktanız Orjindedir")
elif (x2 == 0 and y2 > 0):
    print("İkinci Noktanız Y Ekseni Üstündedir")
elif (x2 == 0 and y2 < 0):
    print("İkinci Noktanız Y Ekseni Üstündedir")
elif (x1 < 0 and y1 == 0):
    print("Birinci Noktanız X Ekseni Üstündedir")
elif (x1 > 0 and y1 == 0):
    print("Birinci Noktanız X Ekseni Üstündedir")
elif (x2 < 0 and y2 == 0):
    print("İkinci Noktanız X Ekseni Üstündedir")
elif (x2 > 0 and y2 ==0):
    print("İkinci Noktanız X Ekseni Üstündedir")




print("Hesaplanıyor...")


print("x1 - x2:",x1 - x2,"y1 - y2",y1-y2 )
print("Aralarındaki uzaklık",Hipotenüs ** 0.5)


ucgenin_alani = (ToplamX * ToplamY /2)
print("Üçgenin Alani",ucgenin_alani)



