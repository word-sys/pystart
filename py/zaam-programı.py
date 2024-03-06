ad=input("Kullanıcı Adı:")
yıl=int(input("Kaç Yıldır Çalışıyorsunuz: "))
maaş=int(input("Maaşınızı Giriniz: "))
if 0 < yıl <= 5:
    zam = maaş/100*10
    toplam = zam + maaş
    print("Sayın",ad,"zamlı maaşınız",toplam,"Türk Lirası olmuştur.")
elif 6 <= yıl <= 10:
    zam = maaş/100*15
    toplam = zam + maaş
    print("Sayın",ad,"zamlı maaşınız",toplam,"Türk Lirası olmuştur.")
elif 11 < yıl:
    zam = maaş/100*25
    toplam = zam + maaş
    print("Sayın",ad,"zamlı maaşınız",toplam,"Türk Lirası olmuştur.")