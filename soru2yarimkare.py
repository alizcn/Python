sayicek = input ("Dört Basamaklı Sayı Girin :")

ilkiki=sayicek[:2]
soniki=sayicek[2:]
ilkislem=int(ilkiki)+int(soniki)
sonislem=int(ilkislem)*int(ilkislem)

if int(sonislem)==int(sayicek):
    print("Girilen sayı Yarımkare bir sayıdır")
else:
    print("Girilen sayı Yarımkare bir sayı değildir")