def asal(sayi):
    if (sayi == 1 ):
        return False

    elif(sayı == 2 ):
        return True


    else:
        for i in range(2,sayi):
            if sayi % i == 0 :
                return False
        return True

while True:
    sayı = int(input("Sayıyı Giriniz:"))
    if sayı == "q":
        break
    else:
        if asal (sayı):
            print("Sayı Asal Bir Sayıdır..")
        else:
            print("Sayınız Asal Bir Sayı Değildir.")

