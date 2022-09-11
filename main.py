sayi = int(input("Sayi: "))
basamak_sayisi = len(str(sayi))
basamak_sayisi = int(basamak_sayisi)
toplam = 0
gecici_sayi = sayi
for i in range(basamak_sayisi):
    a = int(gecici_sayi) % 10
    print("Basamak:",a)
    b = a ** basamak_sayisi
    toplam += b
    print("Toplanacak sayi:",b,"\n")
    gecici_sayi = gecici_sayi // 10
print("Toplam:",toplam)
if(toplam == sayi):
    print("Armstrong sayisi.")
else:
    print("Armstrong sayisi degil.")
    
    
    
