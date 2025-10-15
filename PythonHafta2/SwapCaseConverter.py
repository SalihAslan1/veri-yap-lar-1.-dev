metin = input("Lütfen dönüştürmek istediğiniz metni girin: ")

if not metin:
    print("\n[UYARI] Metin boş olamaz.")
    exit()

donusmus_metin = metin.swapcase()

print("\n--- Sonuç ---")
print(f"Orijinal Metin:     {metin}")
print(f"Dönüşmüş Metin:     {donusmus_metin}")