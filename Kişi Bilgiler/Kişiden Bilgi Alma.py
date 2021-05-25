print("""**********************
Kullanıcı Girişi
**********************""")
sys_kullanıcı_adı = "Efe"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if(kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola hatalı")
elif(kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı_Adı Hatalı")
elif(kullanıcı_adı !=sys_kullanıcı_adı and sys_parola!= parola):
    print("Tüm Gilgiler Hatalı")
else:
    print("Giriş Yapıldı")
