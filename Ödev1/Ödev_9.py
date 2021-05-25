"""

1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""
a = 1
carpım = 0
while(a <= 10):
    for i in range(1,11):
        print("{} ile {} çarpımı = {}".format(i, a, i * a))
    a+=1





