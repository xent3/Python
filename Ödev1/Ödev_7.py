sayı=int(input("Lütfen sayı giriniz:"))

a = 1
list = []

for i in range(a,sayı):
    if (sayı % a == 0 ):
        list.append(a)
        a+=1
    else:
        a+=1
        continue
print(list)

toplam = 0

for i in list:
    toplam = i + toplam

print("Toplam",toplam)

if(toplam == sayı):
    print("Mükemmel")
else:
    print("Mükemmel Değil")

