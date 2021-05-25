"""

Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""


sayı=input("Lütfen sayı giriniz:")

liste = list(sayı)


print(liste)

üst = int(len(liste))

toplam = 0

for i in liste:
    toplam = toplam + (int(i) ** üst)


if(int(toplam) == int(sayı)):
    print("Armstrong sayısıdır")

else:
    print("Değildir")

