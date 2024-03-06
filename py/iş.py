yaş = int(input("Yaşınız: "))
belge = input("Sürücü belgen var mı: ")
eğitim= input("Eğitim Durumu: ")
if yaş < 40:
    if eğitim == "Üniversite":
        if belge == "Var":
            print("İşe Alındınız.")
        else:
            print("Üzgünüz, kriterlerimize uymuyorsunuz.")
    else:
        print("Üzgünüz, kriterlerimize uymuyorsunuz.")
else:
    print("Üzgünüz, kriterlerimize uymuyorsunuz.")