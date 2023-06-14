
hafif=[]
orta=[]
agir=[]
say=1

while say==1:
    agirlik = int(input("Ağırlık Giriniz:"))
    if agirlik > 0 and agirlik < 50:
        hafif.append(agirlik)
        continue
    elif agirlik>=50 and agirlik<=70:
        orta.append(agirlik)
        continue
    elif agirlik>=70:
        agir.append(agirlik)
        continue
    elif agirlik < 0:
        print("Yanlış Değer Girdiniz")
        continue
    else:
        toplam= len(hafif+orta+agir)
        ortalama=sum(hafif+orta+agir)
        print("Giriş Tamamlandı\n Sonuçlar:\n")
        print("Sporcu Sayısı:", toplam)
        print("Ağırlık ortalaması:", ortalama/toplam)
        print("Hafif Siklet:", len(hafif),"Orta Siklet:",len(orta),"Ağır Siklet:",len(agir))

        break
