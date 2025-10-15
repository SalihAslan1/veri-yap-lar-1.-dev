sayi = 0
print(f"Başlangıç değeri: {sayi}")
print("------------------------")

while True:
    komut = input("Artırmak için (+), Azaltmak için (-), Çıkmak için (q) girin: ")

    if komut == '+':
        sayi += 1
        print(f"Sayı artırıldı. Yeni değer: {sayi}")

    elif komut == '-':
        sayi -= 1
        print(f"Sayı azaltıldı. Yeni değer: {sayi}")

    elif komut.lower() == 'q':
        print("\nÇıkış yapılıyor...")
        print(f"Nihai değer: {sayi}")
        break

    else:
        print("[UYARI] Geçersiz komut. Lütfen sadece '+', '-' veya 'q' girin.")