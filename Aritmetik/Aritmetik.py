print("Programımıza Goş Geldiniz...")
a = 0
liste = []



while(a < 5):
    sayi = str(input("Lütfen değer giriniz:"))
    liste.append(sayi)
    a += 1

liste.sort();
print("Listeniz",liste)

print("-"*50)
print("Hesaplanıyor.....")
print("-"*50)
print("Hesaplandı.....")


toplam =int(liste[0])+int(liste[4])

print("En büyük Ve En Küçük Sayının Toplamının Aritmetik Ortalaması :",toplam/2)












