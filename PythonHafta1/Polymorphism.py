class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim
    def tepki(self):
        raise NotImplementedError('HATA')
class Kedi(Hayvanlar):
    def tepki(self):
        return 'Miyav!'
class Kopek(Hayvanlar):
    def tepki(self):
        return 'Haav! Hav!'
hayvan = [Kedi('Boncuk'),
Kedi('Tekir'),
Kopek('Elmas')]
for hyvn in hayvan:
    print(hyvn.isim + ': ' + hyvn.tepki())