
def kontrol(sayi):
    sayiOrg = sayi
    birler = sayi % 10
    sayi = sayi - birler
    sayi = sayi / 10
    onlar = sayi % 10
    yuzler = (sayi - onlar) / 10
    kontrol = (birler * birler * birler) + (onlar * onlar * onlar) + (yuzler * yuzler * yuzler)
    if sayiOrg == kontrol:
        print(sayiOrg)

sayi=100
while sayi<=999:
    kontrol(sayi)
    sayi+=1