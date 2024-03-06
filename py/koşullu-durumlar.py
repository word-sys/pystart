saat = float(input("Kaç Saattir Park Ediyorsunuz: "))
if 0 < saat <= 1:
    print("Ödeyeceğiniz Ücret: 10 Türk Lirası ya da 0.5379236148466918 Dolar yada 0.5521811154058531 Euro.")
elif 1 < saat <= 2:
    print("Ödeyeceğiniz Ücret: 20 Türk Lirası ya da 1.075847229693384 Dolar yada 1.104362230811706 Euro.")
elif 2 < saat:
    print("Ödeyeceğiniz Ücret: ",int(saat*10)," Türk Lirası ya da",saat*0.5379236148466918,"Dolar yada",saat*0.5521811154058531,"Euro.")