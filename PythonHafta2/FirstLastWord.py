metin = input("Lütfen bir metin girin: ").strip()

if not metin:
    print("\n[UYARI] Metin boş olamaz.")
    exit()

kelime_listesi = metin.split()

ilk_kelime = kelime_listesi[0]

son_kelime = kelime_listesi[-1]

print("\n--- Sonuç ---")
print(f"Girdiğiniz Metin: \"{metin}\"")
print(f"Toplam Kelime Sayısı: {len(kelime_listesi)}")
print(f"İlk Kelime: {ilk_kelime}")
print(f"Son Kelime: {son_kelime}")