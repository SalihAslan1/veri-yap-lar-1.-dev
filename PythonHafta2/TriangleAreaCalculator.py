import math


try:
    kenar_a = float(input("Lütfen birinci kenar (a) uzunluğunu girin: "))
    kenar_b = float(input("Lütfen ikinci kenar (b) uzunluğunu girin: "))
    kenar_c = float(input("Lütfen üçüncü kenar (c) uzunluğunu girin: "))

except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen sadece sayı kullanın.")
    exit()

if kenar_a <= 0 or kenar_b <= 0 or kenar_c <= 0:
    print("\n[HATA] Kenar uzunlukları pozitif olmalıdır.")
    exit()

if (kenar_a + kenar_b <= kenar_c) or \
   (kenar_a + kenar_c <= kenar_b) or \
   (kenar_b + kenar_c <= kenar_a):
    print("\n[HATA] Girilen kenar uzunlukları bir üçgen oluşturmamaktadır (Üçgen Eşitsizliğini sağlamıyor).")
    exit()

yari_cevre_s = (kenar_a + kenar_b + kenar_c) / 2

alan_kok_ici = yari_cevre_s * (yari_cevre_s - kenar_a) * \
               (yari_cevre_s - kenar_b) * (yari_cevre_s - kenar_c)

ucgen_alani = math.sqrt(alan_kok_ici)

print("\n--- Hesaplama Sonuçları ---")
print(f"Kenar Uzunlukları: a={kenar_a}, b={kenar_b}, c={kenar_c}")
print(f"Yarı Çevre (s):    {yari_cevre_s:.2f}")
print(f"Üçgenin Alanı:     {ucgen_alani:.2f} birim kare")