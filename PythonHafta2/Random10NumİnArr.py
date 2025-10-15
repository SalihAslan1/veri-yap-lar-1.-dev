import random

rastgele_sayilar = []

uretilecek_adet = 10

alt_sinir = 1
ust_sinir = 100

for _ in range(uretilecek_adet):
    yeni_sayi = random.randint(alt_sinir, ust_sinir)

    rastgele_sayilar.append(yeni_sayi)

print(f"Üretilen Sayı Adedi: {uretilecek_adet}")
print(f"Sayı Aralığı: {alt_sinir} ile {ust_sinir} arası")
print("\n--- Rastgele Üretilen Sayılar Dizisi ---")
print(rastgele_sayilar)