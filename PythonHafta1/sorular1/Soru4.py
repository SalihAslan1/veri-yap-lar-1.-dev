class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

hesap_makinesi = HesapMakinesi()

sonuc1 = hesap_makinesi.topla(10, 20)
print("İki sayının toplamı:", sonuc1)

sonuc2 = hesap_makinesi.topla(10, 20, 30)
print("Üç sayının toplamı:", sonuc2)
