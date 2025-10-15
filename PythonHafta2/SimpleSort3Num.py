try:
    sayi1 = float(input("Lütfen birinci sayıyı girin: "))
    sayi2 = float(input("Lütfen ikinci sayıyı girin: "))
    sayi3 = float(input("Lütfen üçüncü sayıyı girin: "))

except ValueError:
    print("\n[HATA] Geçersiz sayı girdisi. Lütfen sadece rakam kullanın.")
    exit()

sayilar = [sayi1, sayi2, sayi3]

sirali_sayilar = sorted(sayilar)

print("\n--- Sonuç ---")
print(f"Girdiğiniz sayılar: {sayi1}, {sayi2}, {sayi3}")
print(f"Küçükten Büyüğe Sıralama: {sirali_sayilar}")