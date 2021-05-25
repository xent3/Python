print("Welcome To My Programe...")

def ebob_hesapla(sayi1,sayi2):
    if sayi1 < sayi2:
        for i in range(1,sayi1+1):
            if not(sayi1 % i) and not(sayi2 % i ):
                ebob = i
    return ebob





while True:
    sayi = input("Lütfen bir sayı giriniz:")
    sayi1 = input("Lütfen bir sayı giriniz:")
    if sayi == "q" and sayi1 == "q":
        print("Programdan Çıkıyorsunuz..")
        break
    else:
        print(ebob_hesapla(int(sayi),int(sayi1)))