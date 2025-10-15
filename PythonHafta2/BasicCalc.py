sayi1 = float(input("Lütfen birinci sayıyı girin: "))
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))

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
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        islem_adi = "Bölme"
    else:
        print("\nHATA: Sıfıra bölme yapılamaz!")
        exit()
else:
    print("\nHATA: Geçersiz bir işlem seçimi yaptınız.")
    exit()

print("\n--- Hesaplama Sonucu ---")
print(f"İşlem Tipi: {islem_adi}")
print(f"İşlem: {sayi1} {islem} {sayi2}")
print(f"Sonuç: {sonuc}")