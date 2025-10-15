#%% constructor veya (or) initializer metot
class Hayvan():
    def __init__(self,isim,yas): #yapıcı/constructor metot
        self.isim=isim
        self.yas=yas

    def getYas(self):
        return self.yas

    def getAd(self):
        return self.isim

h1=Hayvan("dog",2)
h1_yas=h1.getYas()

print("h1 in yaşı :",h1_yas)

h1_isim=h1.getAd()

print("h1 in isim :",h1_isim)

h2=Hayvan("cat",3)
h2_yas=h2.getYas()

print("h2 in yaşı :",h2_yas)