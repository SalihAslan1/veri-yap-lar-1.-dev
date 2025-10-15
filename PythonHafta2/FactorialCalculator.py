try:
    sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin (Pozitif Tam Sayı): "))
except ValueError:
    print("\n[HATA] Lütfen geçerli bir tam sayı girin.")
    exit()

if sayi < 0:
    print("\n[HATA] Faktöriyel sadece pozitif tam sayılar veya sıfır için tanımlanmıştır.")
    exit()
elif sayi == 0:
    faktoriyel = 1
    acilim = "1"
else:
    faktoriyel = 1
    acilim_listesi = []

    for i in range(sayi, 0, -1):
        faktoriyel *= i
        acilim_listesi.append(str(i))

    acilim = " x ".join(acilim_listesi)

print("\n--- Sonuç ---")

if sayi == 0:
    print(f"{sayi}! = {faktoriyel}")
else:
    print(f"{sayi}! = {acilim} = {faktoriyel}")