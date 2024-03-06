urun1 = int(input("Ürün 1 Fiyat: "))
urun2 = int(input("Ürün 1 Fiyat: "))
if urun1+urun2 <= 200:
    toplam = urun1+urun2
    print("Ödenecek Miktar: ",toplam,"TL dir.")
elif urun1+urun2 > 200:
    toplam= urun1+urun2
    indirim = toplam/100*25
    indirimli_fiyat = toplam-indirim
    print("Ödenecek Miktar",toplam,"İndirimden Sonra",indirimli_fiyat,"TL dir.")
