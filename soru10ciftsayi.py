ilksayi=input("İlk Sayıyı Giriniz:")
ikincisayi=input("İkinci Sayıyı Giriniz:")


say=0

for i in range(int(ilksayi), int(ikincisayi)):
    if i%2==0:
        say = say + 1
        print(i)
if int(ikincisayi)%2==0:
    print(ikincisayi)
    say=say+1
print("Başlangıç ve bitiş değeri:",ilksayi,ikincisayi)
print("Toplamda",say,"sayı bulunmaktadır")

