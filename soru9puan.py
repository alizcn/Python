ales = float(input("Ales:"))
yds = float(input("Yds:"))
mno = float(input("Mezuniyet Ortalaması:"))

siralama=(((50 / 100) * float(ales))+((25 / 100) * float(yds))+((25 / 100) * float(mno)))
print(siralama)

if siralama>=60:
    print("Sıralamaya girebilir")
else:
    print("Sıralamaya giremez")

