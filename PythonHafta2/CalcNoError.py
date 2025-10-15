try:
    sayi1 = float(input("Lütfen birinci sayıyı girin: "))
    sayi2 = float(input("Lütfen ikinci sayıyı girin: "))

except ValueError:
    print("\n[HATA] Geçersiz sayı girdiniz. Lütfen sadece rakam kullanın.")
    exit()

islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")

sonuc = 0

if islem == '+':
    sonuc = sayi1 + sayi2
    islem_adi = "Toplama"
elif islem == '-':
    sonuc = sayi1 - sayi2
    islem_adi = "Çıkarma"
elif islem == '*':
    sonuc = sayi1 * sayi2
    islem_adi = "Çarpma"
elif islem == '/':
    if sayi2 == 0:
        print("\n[HATA] Bir sayıyı sıfıra bölemezsiniz.")
        exit()
    else:
        sonuc = sayi1 / sayi2
        islem_adi = "Bölme"
else:
    print("\n[HATA] Geçersiz bir işlem seçimi yaptınız. (+, -, *, / kullanın)")
    exit()

print("\n--- Hesaplama Sonucu ---")
print(f"İşlem Tipi: {islem_adi}")
print(f"İşlem: {sayi1} {islem} {sayi2}")
print(f"Sonuç: {sonuc}")