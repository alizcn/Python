
yas = int(input("Yaşınızı Giriniz :"))
boy = float(input("Boy (m):"))
kilo = float(input("Kilo (kg):"))
vki = kilo / (boy * boy)
print("VKİ:",vki)

if yas<=17 and yas>=13 and vki<=24.99 and vki>=18.50:
    print("Tebrikler askeri liseye girebilirsiniz")
else:
    print("Askeri liseye giremezsiniz.")