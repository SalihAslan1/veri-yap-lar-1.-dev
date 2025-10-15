class Arac():
    renk="sarı"
    model="jeep"
    marka="kia"

a1=Arac()

print(a1) #a1 bir objedir çıktısı veriyor.
print(a1.marka)
print(a1.model)
print(a1.renk)
a1.marka="BMW"
print(a1.marka)
#%% Metotlar
class Kare():
    kenar=10 #metre
    def alan(self):
        alan=self.kenar*self.kenar
        print("Alan",alan)

k1=Kare()
print(k1)
print(k1.kenar)
print(k1.alan())