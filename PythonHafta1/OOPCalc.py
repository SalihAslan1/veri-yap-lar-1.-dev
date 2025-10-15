# -*- coding: utf-8 -*-
"""
OOP ile Hesap makinesi
@author: msinan
"""
class Makine():
    "hesap makinesi"
    def __init__(self,a,b):
        "başlangıç değerlerini ayarlar"
        #öznitelik alır
        """ pass """
        self.deger1=a
        self.deger2=b
        # pass
        #sonra oluşturursak pass
    def topla(self):
        " toplama a+b = sonuc -> return sonucs"
        sonuc=self.deger1+self.deger2
        return sonuc
        """pass"""
    def carp(self):
        "carpma a*b= sonuc -> return sonuc"
        sonuc=self.deger1*self.deger2
        return sonuc
        """pass"""
    def cikar(self):
        return self.deger1-self.deger2
    def bol(self):
        return self.deger1/self.deger2
x=5
y=2
h: Makine=Makine(x,y)
tSonuc=h.topla()
cSonuc=h.carp()
print("toplama sonuc: {}, çarpma sonucu: {}".format(tSonuc,cSonuc))