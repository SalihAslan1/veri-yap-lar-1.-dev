besin_katlari = []

for sayi in range(-100, 101, 5):
    besin_katlari.append(sayi)

sayi_metinleri = [str(s) for s in besin_katlari]

yan_yana_sayilar = ", ".join(sayi_metinleri)

print(f"--- -100 ile +100 Arasında 5'in Katları ({len(besin_katlari)} adet) ---")
print(yan_yana_sayilar)