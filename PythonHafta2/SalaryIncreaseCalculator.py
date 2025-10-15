try:
    mevcut_maas = float(input("Lütfen mevcut maaşı (TL) girin: "))

    zam_orani = float(input("Lütfen uygulanacak zam oranını (%) girin: "))

except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen sadece rakam kullanın.")
    exit()

if mevcut_maas < 0 or zam_orani < 0:
    print("\n[HATA] Maaş ve zam oranı negatif olamaz.")
    exit()

zam_miktari = mevcut_maas * (zam_orani / 100)

yeni_maas = mevcut_maas + zam_miktari

print("\n--- Zam Hesaplama Sonuçları ---")
print(f"Mevcut Maaş:           {mevcut_maas:,.2f} TL")
print(f"Uygulanan Zam Oranı:   %{zam_orani:,.2f}")
print("---------------------------------")
print(f"Zam Miktarı:           {zam_miktari:,.2f} TL")
print(f"Zamlı Yeni Maaş:       {yeni_maas:,.2f} TL")