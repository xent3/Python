boy=float(input("Lütfen boyunuzu giriniz:"))
kilo=float(input("Lütfen kilonuzu giriniz:"))
bdi=(kilo / (boy * boy))
print(bdi)

if (bdi < 18.5):
    print("Zayıf")
elif (18.5 <= bdi <= 25):
    print("Normal")
elif(25 <= bdi <= 30):
    print("Kilolu")
elif(bdi > 30):
    print("Obez")



