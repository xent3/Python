"""
2.dereceden bilinmeyenli bir denklemin koklerini bulma

Denklem : ax^2 + bx + c


Detaylı Hesaplama : b ** 2 - 4 * a *c

Birinci kok : (-b -delta  ** 0.5) / (2*a)
İkinci kok :  (-b + delta ** 0.5) / (2*a)
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))


delta = b**2 - 4 * a * c


x1 = (-b -delta  ** 0.5) / (2*a)
x2 = (-b +delta  ** 0.5) / (2*a)

print ("Birinci Kok : {}\nİkinci Kok : {}\n".format(x1,x2))