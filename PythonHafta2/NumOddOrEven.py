girilen_sayi = int(input("Lütfen bir tam sayı girin: "))

kalan = girilen_sayi % 2

if kalan == 0:
    print(f"Girdiğiniz sayı ({girilen_sayi}) ÇİFT sayıdır.")
else:
    print(f"Girdiğiniz sayı ({girilen_sayi}) TEK sayıdır.")