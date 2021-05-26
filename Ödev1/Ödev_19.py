def ucgen(x,y,z):
    if(abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(z-y)<x<z+y ):
        return True



while True:
    x = int(input("Lütfen x değerini giriniz:"))
    y = int(input("Lütfen y değerini giriniz:"))
    z = int(input("Lütfen z değerini giriniz:"))

    if (x =="q" or y =="q" or z == "q"):
        break

    if(ucgen(x,y,z)):
        print("Bu değerler ile üçgen oluşabilir")

    else:
        print("Bu değerler ile üçgen oluşamaz")