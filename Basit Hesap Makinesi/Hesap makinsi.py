print ("""**********************
Hesap Makinesi Programı

İşlemler : 

1. Toplama İşlemi 

2.Çıkarma İşlemi 

3.Çarpma İşlemi

4. Bölme İşlemi 
**********************""")

a = int(input("Lütfen bir sayı giriniz:"))
b = int(input("Lütfen başka bir değer giriniz :"))
işlem = int(input("İşlem Sayısı Giriniz :"))


if(işlem == 1 ):
    print("{} ile {} sayılarının toplamı {} ".format(a,b,a+b))
elif(işlem == 2 ):
    print("{} ile {} sayılarının farkı {} ".format(a,b,a-b))
elif(işlem == 3 ):
    print("{} ile {} sayılarının çarpımı {} ".format(a,b,a*b))
elif(işlem == 4):
    print("{} ile {} sayılarının bölümü {} ".format(a,b,a/b))
else:
    print("Geçersiz....")


