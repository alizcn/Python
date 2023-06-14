yakittuketcek = float(input ("Km başına yakit tüketimi (lt):"))
yakitfiyatcek = float(input ("1 lt yakıtın fiyatı (TL):"))
yolcek = float(input ("Aracın katettiği toplam yol (km):"))

kaclitre=yolcek*yakittuketcek
toplamyakit=kaclitre*yakitfiyatcek

print("Toplam Yakıt Tutarı:",toplamyakit,"TL")