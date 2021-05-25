print("Kolay Olan Programıma hoş Geldiniz!!!! :CCCC")
a = 1
liste1 = [1,2,5]
liste2 = [8,2,3]
liste3 = [1,9,2]
matris = liste1 + liste2 + liste3
print(matris)


while(a < 10 ):
    if(matris.count(a) != 0):
        print("Bu Listede {} sayısı {} defa vardır".format(a, matris.count(a)))
#        print("Bu Listede {} sayısı hiç yoktur.".format(a,))
        print("-"*50)
    a += 1


































