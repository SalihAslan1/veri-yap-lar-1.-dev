try:
    tekrar_sayisi = int(input("Lütfen tekrarlanacak sayıyı girin (Örn: 5): "))
except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen tam sayı kullanın.")
    exit()

if tekrar_sayisi <= 0:
    print("\n[HATA] Lütfen pozitif bir tam sayı girin.")
    exit()

sayi_metin = str(tekrar_sayisi)

tekrarli_sonuc = sayi_metin * tekrar_sayisi

print("\n--- Sonuç ---")
print(f"Girdiğiniz Sayı: {tekrar_sayisi}")
print(f"Tekrarlı Sonuç: {tekrarli_sonuc}")