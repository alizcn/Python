def kdv_hesapla(kdvoran, kdvdahil):
    kdvharicfiyat = (int(kdvdahil) / ((float(kdvoran)/100)+1))
    kdvorani =  int(kdvdahil) - int(kdvharicfiyat)
    print ("Kdv :",kdvorani)
    print("Kdv Hariç Fiyat :", kdvharicfiyat)
    return kdvharicfiyat,kdvorani

kdvvv = input("Kdv Oran :")

kdvdahiiil = input("Kdv Dahil Fiyat : ")

kdv_hesapla(kdvvv, kdvdahiiil)



