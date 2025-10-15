toplam = 0
sayac = 0

try:
    adet = int(input("Kaç adet sayı gireceksiniz? "))

    if adet <= 0:
        print("\n[HATA] Girilecek sayı adedi pozitif olmalıdır.")
        exit()

    print("--------------------------------")

    for i in range(adet):
        girilen_sayi = float(input(f"Lütfen {i + 1}. sayıyı girin: "))
        toplam += girilen_sayi
        sayac += 1

except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen sadece sayı kullanın.")
    exit()

ortalama = toplam / sayac

print("\n--- Sonuçlar ---")
print(f"Toplam Girilen Sayı Adedi: {sayac}")
print(f"Sayıların Toplamı: {toplam:.2f}")
print(f"Sayıların Ortalaması: {ortalama:.2f}")