sayi_metin = input("Lütfen rakamlarının toplamını bulmak istediğiniz bir tam sayı girin: ")

rakamlar_toplami = 0
acilim_listesi = []

if not sayi_metin.isdigit():
    print("\n[HATA] Lütfen sadece tam sayı rakamları girin.")
    exit()

for rakam in sayi_metin:
    rakam_degeri = int(rakam)

    rakamlar_toplami += rakam_degeri

    acilim_listesi.append(rakam)

acilim = " + ".join(acilim_listesi)

print("\n--- Sonuç ---")
print(f"Girilen Sayı: {sayi_metin}")
print(f"Rakamların Açılımı: {acilim}")
print(f"Rakamların Toplamı: {rakamlar_toplami}")