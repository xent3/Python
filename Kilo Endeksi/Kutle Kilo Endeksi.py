print("""**********************
Menü 
*Beden Kitle İndeksi Hesaplama 
**********************""")
kilo = float(input("Lütfen Kilonuzu Giriniz:"))
boy = float(input("Lütfen Boyunuzu Metre Cinsinden Giriniz:"))
bki = kilo / (boy * boy)

if(bki < 18.5):
    print("Zayıfısınız...")
elif( 18.5<bki and bki<25 ):
    print("Boy Kitle İndeksiniz: Normal...")
elif(25<bki and bki<30):
    print("Kilolusunuz...")
elif (30<bki):
    print("Obezsiniz..")
else:
    ("Hatalı Giriş....")
print ("Kütle Boy İndeksiniz : {}".format(bki))




