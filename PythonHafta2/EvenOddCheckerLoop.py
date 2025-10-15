print("--- Tek/Çift Sayı Kontrol Programı ---")
print("Çıkmak için 'q' veya 'Q' yazıp ENTER tuşuna basın.")
print("---------------------------------------")

while True:
    girdi = input("Lütfen bir tam sayı girin: ")

    if girdi.lower() == 'q':
        print("\nProgram sonlandırılıyor. Hoşça kalın!")
        break

    try:
        sayi = int(girdi)
    except ValueError:
        print("[UYARI] Geçersiz girdi. Lütfen tam sayı veya 'q' girin.")
        continue

    if sayi % 2 == 0:
        sonuc = "ÇİFT"
    else:
        sonuc = "TEK"

    print(f"Girdiğiniz sayı ({sayi}) bir {sonuc} sayıdır.")