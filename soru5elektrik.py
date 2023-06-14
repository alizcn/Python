ilk_endex=int(input("İlk Endeksi Giriniz:"))
son_endex=int(input("Son Endeksi Giriniz:"))
ebirimf=0.159838
if ilk_endex < son_endex:
    tuketim=round(son_endex-ilk_endex,2)
    ebedel=round(tuketim*ebirimf,2)
    kdv=round(ebedel*0.22,3)
    odenecek_tutar=round(ebedel+kdv,3)
    print("Tüketim Miktarınız:",tuketim)
    print("Tüketim Bedeliniz:",ebedel)
    print("KDV Tutarınız %22:",kdv)
    print("Fatura Bedeliniz :",odenecek_tutar)
else:
    print("Lütfen Endexlerinizi Kontrol Ediniz! İlk Endeks Son Endeks'ten Büyük ve Eşit Olamaz!")
