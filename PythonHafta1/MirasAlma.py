#ata sınıf --- parent
class Animal():
    def __init__(self):
        print("hayvan sınıfının yapıcı metotum")
    def sesCikar(self):
        print("hav,miyav,vak....")
    def hareket(self):
        print("zıplar,koşar,yürür..")
#cocuk sınıf ----child
class kedi(Animal):
    def __init__(self):
        super().__init__() # yazmasakta olur ata sınıfın init metodunu ezeriz metot overriding!!
        print("kedi sınıfı oluşturuldu")
    def sesCikar(self):
        print("miyav")
    def DokuzCan(self): #diğer hayvanlardan ayrılan bir fonksiyon :D
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")

k1=kedi()
k1.sesCikar() #ata sınıfı ezer
k1.hareket()
k1.DokuzCan()

class kus(Animal):
    def __init__(self):
        print("kus sınıfı oluşturldu")
    def ucma(self):
        print("kanatları vardır uçarlar")
kus1=kus()
kus1.ucma()
kus1.hareket()