sayicek = input ("Dört Basamaklı Sayı Girin :")

ilkiki=sayicek[:2]
soniki=sayicek[2:]
ilkislem=int(ilkiki)*int(soniki)

ilkters=ilkiki[::-1]
sonikiters=soniki[::-1]
sonislem=int(ilkters)*int(sonikiters)

if (ilkislem==sonislem):
    print("Girilen Sayı TersYüz Sayıdır.")
else:
    print("Girilen Sayı Tersyüz Değildir.")








