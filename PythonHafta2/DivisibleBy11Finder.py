alt_sinir = 1
ust_sinir = 300

onbire_bolunenler = []

for sayi in range(alt_sinir, ust_sinir + 1):

    if sayi % 11 == 0:
        onbire_bolunenler.append(sayi)

print(f"--- {alt_sinir} ile {ust_sinir} Arasında 11'e Bölünen Sayılar ({len(onbire_bolunenler)} adet) ---")

sonuc_yazisi = ", ".join(str(s) for s in onbire_bolunenler)
print(sonuc_yazisi)