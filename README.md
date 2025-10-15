# veri-yap-lar-1.-dev

sorular1.docx dosyası 1.soru cevabı

Bu kod, Nesneye Dayalı Programlamanın (OOP) temelini oluşturan Araba adında bir şablon (sınıf) tanımlıyor. Bu şablon, __init__ (yapıcı) metodu sayesinde, yeni bir araba oluşturulurken onun marka ve model özelliklerini alıp kaydediyor. Ayrıca bilgileri_yazdir adında bir metot içeriyor; bu metot, o arabanın kaydedilmiş marka ve modelini ekrana yazdırıyor. Kodun son kısmında ise bu şablondan araba1 adında somut bir nesne ("Toyota", "Corolla" verileriyle) oluşturuluyor ve ardından bu nesnenin bilgileri ekrana yazdırılarak çıktı alınıyor. Kısacası, bu kod araba özelliklerini düzenli bir yapıda tutmayı ve göstermeyi sağlıyor.


python giriş.pdf dosyası içindeki soruların cevapları

1.Hangi keyword ile sınıf tanımlanır
A. def
B. class
C. return
D. __init
E. Hiçbiri
Cevap: B

2.Hangisi ile python kodu yazılamaz
A. Notepad++
B. jupyter
C. spyder
D. pycharm
E. chromepy
Cevap: E

3.Nesneye dayalı programlama ile ilgili değildir.
A. Sınıf yapısı ile nesne türetilir
B. Sınıflar içeriği olarak, nitelik,metotlar olur
C. Bir sınıftan birden çok nesne türetilemez
D. Metotlar sınıftan türetilen nesnelerin davranışlarıdır.
E. Sınıfların özellikleri public,private,protected,internal..gibi erişimler alabilir.
Cevap: C

4.python dosya uzantısı hangisidir.
A. .pyt
B. .py
C. .ps
D. .ph
E. .pt
Cevap: B

5.Hangisi ile fonksiyon oluşturulur.
A. create fonksiyon1():
B. def fonksiyon1():
C. func fonksiyon1():
D. class fonksiyon1():
E. **init__ fonksiyon1():
Cevap: B

6. bir sınıftan yeni ve eşsiz bir örnek(instance) oluşturmak için hangisi gerekli
A. class
B. return
C. constructors
D. def
Cevap: C

-------------------------------------------------------------------------------

1.Hangisi encapsulation tanımıdır
A. Bir sınıftan yeni eleman türetme işlemine denir
B. Ata sınıfın özelliklerini almaya denir
C. Bir nesnenin metot ve verilerini diğer nesnelerden saklayarak erişime engelleyerek
yanlış kullanımı engel olmaktır
Cevap: C

2. yandaki koda ile ilgili bilgilerden hangisi                      class A():
doğrudur.                                                             def __init__(self,a):
A. A sınıfı B den miras alır.                                           print(“a sınıfı oluşturuldu”)
B. B sınıfı A dan miras alır.                                         def ilk(self):
C. B sınıfı A dan miras alır.Ama tüm                                    print(“ ilk isimli metot”)
özelliklerini almaz                                                 class B(A):
                                                                      def __init__(self,j=10):
                                                                        self.j=j
 Cevap: B

3.Hangisi soyut sınıf (abstract class) tanımıdır
A. Bir sınıftan başka sınıf türetebilmek için oluşturulur.
B. OOP de nesnesi olmayan sınıflara verilen isimdir.
C. Bir sınıfın üst sınıftan miras almasına denir.
Cevap: B 

class Animal(): a.sesVer() ve k.sesVer() çıktısı nedir?
def sesVer(self):
print("ses çıkarırlar")
class kedi(Animal):
def sesVer(self): #ata sınıfı ezdi
print("miyav")
a=Animal()
a.sesVer() ------------------------------→ çıktı ??   ses çıkarırlar
k=kedi()
k.sesVer() ------------------------------→ çıktı ??   miyav
