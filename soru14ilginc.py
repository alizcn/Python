
def kontrol(sayi):
    sayiOrg = sayi
    birler = int(sayi % 10)
    sayi = sayi - birler
    sayi = sayi / 10
    onlar = int(sayi % 10)
    sayi = sayi - onlar
    sayi = sayi / 10
    yuzler = int(sayi % 10)
    sayi = sayi - yuzler
    sayi = sayi / 10
    binler = int(sayi % 10)

    ilk = str(binler) + str(yuzler)
    son = str(onlar) + str(birler)
    topla=int(ilk)+int(son)
    kontrol = int(topla*topla)
    if sayiOrg == kontrol:
        print(sayiOrg)

sayi=1000
while sayi<=9999:
    kontrol(sayi)
    sayi+=1






"""
sayi=2025

birler = int(sayi % 10)
sayi = sayi - birler
sayi = sayi / 10
onlar = int(sayi % 10)
sayi=sayi-onlar
sayi = sayi /10
yuzler=int(sayi%10)
sayi=sayi-yuzler
sayi = sayi /10
binler=int(sayi%10)

ilk=str(binler)+str(yuzler)
son=str(onlar)+str(birler)

print(ilk)
print(son)
print(int(ilk)+int(son))
print(binler,yuzler,onlar,birler)
"""


"""
def kontrol(sayi):
    sayiOrg = sayi
    birler = sayi % 10
    sayi = sayi - birler
    sayi = sayi / 10
    onlar = sayi % 10
    yuzler = (sayi - onlar) / 10
    kontrol = (birler * onlar * yuzler) * (birler + onlar + yuzler)
    if sayiOrg == kontrol:
        print(sayiOrg)

sayi=100
while sayi<=999:
    kontrol(sayi)
    sayi+=1
"""