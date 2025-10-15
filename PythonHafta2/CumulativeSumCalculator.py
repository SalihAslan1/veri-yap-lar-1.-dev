girdi_metni = input("Lütfen sayıları virgül ile ayırarak girin (Örn: 4, 1, 5, 2): ").strip()

if not girdi_metni:
    print("\n[UYARI] Sayı girişi boş olamaz.")
    exit()

try:
    sayi_listesi = [float(s.strip()) for s in girdi_metni.split(',')]
except ValueError:
    print("\n[HATA] Geçersiz sayı formatı. Lütfen sayıları doğru formatta girin.")
    exit()

kumulatif_toplam_listesi = []

anlik_toplam = 0

for sayi in sayi_listesi:
    anlik_toplam += sayi

    kumulatif_toplam_listesi.append(anlik_toplam)

print("\n--- Sonuç ---")
print(f"Orijinal Sayı Dizisi: {sayi_listesi}")
print(f"Kümülatif Toplam Dizisi: {kumulatif_toplam_listesi}")