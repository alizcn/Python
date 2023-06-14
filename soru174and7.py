ilksayi=input("İlk Sayıyı Giriniz:")
ikincisayi=input("İkinci Sayıyı Giriniz:")

say=0

for i in range(int(ilksayi), int(ikincisayi)):
    if i%4==0 and i%7==0:
        say = say + 1
        print(i)
if int(ikincisayi)%4==0 and int(ikincisayi)%7==0 :
    print(ikincisayi)
    say = say + 1
print("Başlangıç ve bitiş değeri:",ilksayi,ikincisayi)
print("Toplamda",say,"sayı bulunmaktadır")

