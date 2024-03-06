eğitim=input("Öğrenci Misiniz: ")
yaş=int(input("Yaşınızı Giriniz:"))
gazi=input("Gazi Yakınımısınız: ")
if yaş < 30 and eğitim=="Evet":
    print("Öğrenci Kartınız Bulunmakta İndirimli.")
elif yaş >= 65 and eğitim=="Hayır":
    print("Yaşlı Kartınız Ücretsizdir.")
elif gazi=="Evet":
    print("Geçişiniz Ücretsizdir.")
else:
    print("Normal Kart kullanıyorsunuz.")