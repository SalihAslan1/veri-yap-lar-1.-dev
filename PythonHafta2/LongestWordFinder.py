metin = input("Lütfen bir cümle veya metin girin: ").strip()

if not metin:
    print("\n[UYARI] Metin boş olamaz.")
    exit()

kelime_listesi = metin.split()

if not kelime_listesi:
    print("\n[UYARI] Metinde geçerli kelime bulunamadı.")
    exit()

en_uzun_kelime = ""
en_uzun_uzunluk = 0

for kelime in kelime_listesi:
    mevcut_uzunluk = len(kelime)

    if mevcut_uzunluk > en_uzun_uzunluk:
        en_uzun_uzunluk = mevcut_uzunluk
        en_uzun_kelime = kelime

print("\n--- Sonuç ---")
print(f"Girdiğiniz Metin: \"{metin}\"")
print(f"En Uzun Kelime: {en_uzun_kelime}")
print(f"Uzunluğu: {en_uzun_uzunluk} karakter")