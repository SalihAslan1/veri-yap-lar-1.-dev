class Animal():
    def sesVer(self):
        print("ses çıkarırlar")
class kedi(Animal):
    def sesVer(self): #ata sınıfı ezdi
        print("miyav")
a=Animal()
a.sesVer()
k=kedi()
k.sesVer()