ilksayi=input("İlk Sayıyı Giriniz:")
ikincisayi=input("İkinci Sayıyı Giriniz:")

say=0
toplanan=[]

for i in range(int(ilksayi), int(ikincisayi)):
    if i%3==0 or i%11==0:
        say = say + 1
        print(i)
        toplanan.append(i)
if int(ikincisayi)%3==0 or int(ikincisayi)%11==0 :
    say = say + 1
    print(ikincisayi)
    toplanan.append(i)

toplam=sum(toplanan)
print("Başlangıç ve bitiş değeri:", ilksayi,"---", ikincisayi)
print("Toplamda",say,"sayı bulunmaktadır")
print("Tüm sayılar toplamı:", toplam)

