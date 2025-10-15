try:
    sayi = int(input("Lütfen asal çarpanlarını bulmak istediğiniz bir tam sayı girin: "))
except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen tam sayı kullanın.")
    exit()

if sayi <= 1:
    print(f"\n[UYARI] {sayi} sayısının asal çarpanı yoktur.")
    exit()

asal_carpanlar = []

bolen = 2
gecici_sayi = sayi

while gecici_sayi > 1:

    if gecici_sayi % bolen == 0:

        asal_carpanlar.append(bolen)
        gecici_sayi = gecici_sayi // bolen

    else:
        bolen += 1

print("\n--- Sonuç ---")
print(f"Girilen Sayı: {sayi}")
print(f"Asal Çarpanları: {asal_carpanlar}")

carpanlar_metni = " x ".join(str(c) for c in asal_carpanlar)
print(f"Açılımı: {sayi} = {carpanlar_metni}")