import random

MIN_SAYI = 1
MAX_SAYI = 100

try:
    adet = int(input(f"Lütfen {MIN_SAYI} ile {MAX_SAYI} arasında kaç adet benzersiz sayı üretmek istediğinizi girin: "))
except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen tam sayı kullanın.")
    exit()

if not (0 < adet <= (MAX_SAYI - MIN_SAYI + 1)):
    print(f"\n[HATA] Üretilecek sayı adedi, {MIN_SAYI} ve {MAX_SAYI} arasındaki toplam sayı adedini (100) geçemez ve sıfırdan büyük olmalıdır.")
    exit()

sayi_havuzu = range(MIN_SAYI, MAX_SAYI + 1)

benzersiz_sayilar = random.sample(sayi_havuzu, adet)

print("\n--- Sonuç ---")
print(f"Aralık: {MIN_SAYI} - {MAX_SAYI}")
print(f"Üretilen Adet: {adet}")
print("Üretilen Benzersiz Sayılar:")
print(benzersiz_sayilar)
