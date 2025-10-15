from abc import ABC, abstractmethod
class Animal(): # super clas
    pass
class kus(Animal):
    pass
a=Animal()

from abc import ABC, abstractmethod
class Animal(ABC): # super clas
    @abstractmethod
    def yurume(self): pass

    @abstractmethod
    def kosma(self): pass #sablon oluşturup tekrar tekrar kullan

class kus(Animal):
    def __init__(self):
        print("kuş oluşturuldu")

    def yurume(self):
        print("kuslar pek yürümez")

    def kosma(self):
        print("kuslar pek kosmazda")

#a=Animal() soyut sınıflardan nesne oluşturulmaz.
b=kus() #abstract clasın içeriği yavru sınıfta doldurulur.
b.kosma()
b.yurume()