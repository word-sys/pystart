bagaj=int(input("Bagaj Kilogramımı Giriniz: "))
if bagaj <= 20:
    print("Herhangi Bir Ücret Ödemenize Gerek Yok.")
elif bagaj > 20:
    toplam = bagaj - 20
    print("Bagaj hakkınızdan fazla kg bulundurmaktasınız. Ödemeniz gereken ücret: ",toplam*10)