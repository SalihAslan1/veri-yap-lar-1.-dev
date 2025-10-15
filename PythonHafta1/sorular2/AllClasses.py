class Insan():
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        print(f"Insan nesnesi oluşturuldu: {self.ad}")

    def konus(self):
        print(f"{self.ad}: Merhaba, ben genel bir konuşma yapıyorum.")

class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no
        print(f"Hoca nesnesi oluşturuldu, Sicil No: {self.sicil_no}")

    def konus(self):
        print(f"{self.ad}: Bir hoca olarak akademik konular üzerine konuşuyorum.")

    def ders_ver(self):
        print(f"{self.ad} ({self.sicil_no}) şu anda ders veriyor.")

class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman
        print(f"Sekreter nesnesi oluşturuldu, Departman: {self.departman}")

    def konus(self):
        print(f"{self.ad}: Bir sekreter olarak idari işler hakkında konuşuyorum.")

    def randevu_ayarla(self):
        print(f"{self.ad}, {self.departman} departmanında randevu ayarlıyor.")

class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no
        print(f"Ogrenci nesnesi oluşturuldu, Öğrenci No: {self.ogr_no}")

    def konus(self):
        print(f"{self.ad}: Bir öğrenci olarak ödevlerim ve sınavlarım hakkında konuşuyorum.")

    def ders_calis(self):
        print(f"{self.ad} ({self.ogr_no}) şu anda ders çalışıyor.")

print("\n--- NESNE OLUŞTURMA VE TEST ---")

hoca1 = Hoca("Dr. Ahmet", 45, "H-101")
sekreter1 = Sekreter("Ayşe Hanım", 30, "Mali İşler")
ogrenci1 = Ogrenci("Mert Yılmaz", 20, "O-505")

print("\n--- DAVRANIŞ TESTİ ---")
hoca1.konus()
sekreter1.randevu_ayarla()
ogrenci1.ders_calis()

print("\n--- MIRAS ALINAN METOT TESTİ ---")
print(f"Sekreterin yaşı: {sekreter1.yas}")