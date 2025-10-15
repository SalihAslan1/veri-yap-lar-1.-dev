metin = input("Lütfen bir cümle girin: ").strip()

if not metin or not metin.split():
    print("\n[UYARI] Metin boş olamaz veya sadece boşluklardan oluşamaz.")
    exit()

kelime_listesi = metin.split()

ters_kelimeler = []

for kelime in kelime_listesi:
    ters_kelime = kelime[::-1]

    ters_kelimeler.append(ters_kelime)

yeni_cumle = " ".join(ters_kelimeler)

print("\n--- Sonuç ---")
print(f"Orijinal Cümle: \"{metin}\"")
print(f"Dönüştürülmüş Cümle: \"{yeni_cumle}\"")