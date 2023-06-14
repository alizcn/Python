trafikcek = int(input ("Trafik yanlış sayısını giriniz :"))
motorcek = int(input ("Motor yanlış sayısını giriniz :"))
yardimcek = int(input ("İlk Yardım yanlış sayısını giriniz :"))

trafikpuan=(100/50)
motorpuan=(100/40)
yardimpuan=(100/30)

trafikyanlis=trafikpuan*(trafikcek)
motoryanlis=motorpuan*(motorcek)
yardimyanlis=yardimpuan*(yardimcek)

sonuctrafik=100-trafikyanlis
sonucmotor=100-motoryanlis
sonucyardim=100-yardimyanlis

print("Trafik puanınız:",sonuctrafik)
print("Motor puanınız:",sonucmotor)
print("İlk Yardım puanınız:",sonucyardim)

if (sonucyardim>=70 and sonuctrafik>=70 and sonucmotor>=70):
    print("Direksiyon sınavına katılmaya hak kazandınız")

else:
    print("Üzgünüz direksiyon sınavına katılamazsınız")




