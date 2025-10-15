try:
    puan = float(input("Lütfen sayısal notunuzu (0-100 arası) girin: "))

except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen sadece sayı kullanın.")
    exit()

if not (0 <= puan <= 100):
    print("\n[HATA] Not 0 ile 100 arasında olmalıdır.")
    exit()

if puan >= 90:
    harf_notu = "AA"
elif puan >= 80:
    harf_notu = "BA"
elif puan >= 70:
    harf_notu = "BB"
elif puan >= 60:
    harf_notu = "CB"
elif puan >= 50:
    harf_notu = "CC"
elif puan >= 40:
    harf_notu = "DC"
else:
    harf_notu = "FF"

print("\n--- Sonuç ---")
print(f"Girdiğiniz Sayısal Not: {puan:.2f}")
print(f"Harf Karşılığı:         {harf_notu}")

if harf_notu in ["AA", "BA", "BB", "CB", "CC", "DC"]:
    print("Durum: Başarılı (Geçer Not)")
else:
    print("Durum: Başarısız (Kaldı)")
