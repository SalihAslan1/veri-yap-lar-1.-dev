SESLI_HARFLER = "aeıioöuüAEIİOÖUÜ"

metin = input("Lütfen bir metin girin: ")

sesli_harf_sayisi = 0

if not metin:
    print("\n[UYARI] Metin boş olamaz. Sayı 0'dır.")
    exit()

for karakter in metin:

    if karakter in SESLI_HARFLER:
        sesli_harf_sayisi += 1

print("\n--- Sonuç ---")
print(f"Orijinal Metin: \"{metin}\"")
print(f"Metindeki Sesli Harf Sayısı: {sesli_harf_sayisi}")