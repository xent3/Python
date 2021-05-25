print("Hello Guys Welcome To My Programe...")

def tamsayi (sayi):
    liste = []
    for i in range(1, sayi + 1):
        for j in range(1, sayi + 1):
            if i == j:
                if sayi % i == 0:
                    liste.append(i)
    return liste



def ebob (sayi,sayi1):
    liste = []
    liste1 = []
    for i in list(tamsayi(sayi)):
        for j in list(tamsayi(sayi1)):
            if i == j:
                liste.append(i)
    liste1 = max(liste)
    return liste1




while True:
    sayi = input("Lütfen Bir Sayı Giriniz:")
    sayi1 = input("Lütfen Bir Sayı Giriniz:")
    if sayi == "q" and sayi1 == "q" :
        print("Programdan Çıkıyorsunuz...")
        break
    else:
        print("Sayılarınızın Ebob'u :",ebob(int(sayi),int(sayi1)))



















