#%% metotlar
class Isci():
    yas=20
    maas=1000
    def yasaGoreMaasOranla(self):
        print(self.yas/self.maas)

isci1=Isci()
isci1.yasaGoreMaasOranla()

def yasMaasOranı(yas,maas): #class dışı metot
    a=yas/maas
    #print("oran:\t",a)
    print("oran:\t {}".format(a))
yasMaasOranı(20,2000)