print("*"*50)
print("Kullanıcı Girişi Programı..")
print("*"*50)



sys_kullanıcı_adı = "Efe"
sys_parola = "Efebaba"
giris_hakki = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adınızı Giriniz:")
    parola = input("Parola:")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı..")
        giris_hakki -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve parola Hatalı...")
        giris_hakki -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı...")
        break
    if(giris_hakki == 0):
        print("Giriş Hakkınız Bitti..")
        break