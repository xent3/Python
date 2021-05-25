sayı1 = int(input("Lütfen 1.Sayıyı giriniz :"))
sayı2 = int(input("Lütfen 2.Sayıyı giriniz :"))
sayı3 = int(input("Lütfen 3.Sayıyı giriniz :"))
print("Hesaplanıyor....")

if (sayı1>sayı2 and sayı1>sayı3 and sayı2>sayı3):
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı1,sayı2,sayı3))
elif(sayı1>sayı2 and sayı1>sayı3 and sayı3>sayı2):
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı1, sayı3, sayı2))
elif(sayı2>sayı1 and sayı2>sayı3 and sayı1>sayı3):
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı2, sayı1, sayı3))
elif(sayı2>sayı1 and sayı2>sayı3 and sayı3>sayı1):
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı2, sayı3, sayı1))
elif(sayı3>sayı1 and sayı3>sayı2 and sayı1>sayı2):
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı3, sayı1, sayı2))
else:
    print("Sayılar Büyükten Küçüğe {} > {} > {}".format(sayı3, sayı2, sayı1))
