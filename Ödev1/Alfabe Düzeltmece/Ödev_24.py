def duzenleme(list):
    listed = sorted(list, key=str.lower)
    return listed





i = 0
with open("D:\\pc\\Yazılım\\phycharm\\Ödev1\\Alfabe Düzeltmece\\alfabe.txt", "w", encoding="utf-8") as file:
    while True:
        i = input("Lütfen değer giriniz:")
        if (i == "q"):
            break
        file.write("{}\n".format(i))


with open("D:\\pc\\Yazılım\\phycharm\\Ödev1\\Alfabe Düzeltmece\\alfabe.txt", "r", encoding="utf-8") as file:
    liste = []
    for u in file:
        u = u[:-1]
        liste.append(u)
print(liste)

with open("D:\\pc\\Yazılım\\phycharm\\Ödev1\\Alfabe Düzeltmece\\alfabe.txt", "w", encoding="utf-8") as file:
    for en in duzenleme(liste):
        file.write("{}\n".format(en))