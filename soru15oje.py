
sozluk = dict({1:'kırmızı', 2:'yeşil' , 3:'sarı', 4:'siyah'})
say=1
secilen=[]


while say == 1:
    cek = int(input("Kodu girin (1,2,3,4 veya çıkmak için 111):"))
    if cek == 1 or cek == 2 or cek == 3 or cek == 4:
        secilen.append(sozluk[cek])
    elif cek == 111:
        print("Gün Sonu Satış Raporu")
        print("Kırmızı Kalem", secilen.count("kırmızı"), "Yeşil Kalem", secilen.count("yeşil"), "Sarı Kalem", secilen.count("sarı"), "Siyah Kalem", secilen.count("siyah"))
        break
    else:
        print("Hata!! Lütfen geçerli bir kod girin")


