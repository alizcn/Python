sayicek = input ("Dört Basamaklı Sayı Girin :")

ilksayi=sayicek[:1]
ikincisayi=sayicek[1:2]
ucuncusayi=sayicek[2:3]
dorduncusayi=sayicek[3:4]


toplam=int(ilksayi)+int(ikincisayi)+int(ucuncusayi)+int(dorduncusayi)
kup=int(toplam)*int(toplam)*int(toplam)

if int(kup)==int(sayicek):
    print("Girilen" ,sayicek," sayısı Küpünü Dolduran Sayıdır")
else:
    print("Girilen" ,sayicek," sayı Küpünü Dolduran Sayı Değildir")



