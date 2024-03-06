ad = input("Kullanıcı Adı: ")
eğitim = input("Eğitim Durumu: ")
yaş = int(input("Yaşınız: "))
if eğitim == "Lise" or eğitim== "lise" or eğitim == "Üniversite" or eğitim== "üniversite":
    if yaş >= 18:
        print(ad,"Ehliyet Alabilirsiniz.")
    else:
        print(ad,"Yaşınız 18 değil ehliyet alamazsınız.")
else:
    print(ad,"Eğitim Durumunuz Yeterli Değil.")