def sayac(dosya):
    with open(dosya, "r", encoding="utf-8") as file:
        line_count = 0
        for line in file:
            line_count += 1

    return line_count



def arama (deger,dosya):
    with open(dosya, "r", encoding="utf-8") as file:
        var = 0
        for i in file:
            i = i[:-1]
            if (i == deger):
                var += 1
        return var


def bulma(deger,dosya):
    sayac = 1
    sozluk = {}
    with open(dosya, "r", encoding="utf-8") as file:
        for a in file:
            if a[:-1] == deger:
                sozluk [sayac] = deger
                sayac += 1
            else:
                sayac += 1
    return sozluk



i = 0
with open("bilgiler","w",encoding="utf-8") as file:
    while True :
        i = input("Lütfen değer giriniz:")
        if (i == "q"):
            break
        file.write("{}\n".format(i))




cevap = input("Aramak istediğiniz kelimeyi yazınız:")
if(arama(cevap,"bilgiler")):
    print("Aradığın değer {} kere bulundu".format(arama(cevap,"bilgiler")))
else:
    print("Aradığınız kelime bulunamadı")


print(bulma("e","bilgiler"))




