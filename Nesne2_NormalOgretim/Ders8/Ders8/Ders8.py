#class Sinifim:
#    x=10


#nesne1=Sinifim()
#print(nesne1.x)



class Kisi:
    def __init__(self, pAd,pSoyad,pYas):  # init yapıcı metot.  Class oluşunca ilk burası çalışır
        self.ad = pAd
        self.soyad = pSoyad
        self.yas = pYas


    def BilgileriYazdir(self):
        print("Merhaba! Benim adım {0} {1}. {2} yaşındayım".format(self.ad,self.soyad,self.yas))

    
    def YasiDondur(self):
        return self.yas



#kisi1=Kisi("murat","ince",36)
#print(kisi1.ad)
#print(kisi1.soyad)
#print(kisi1.yas)
#kisi1.BilgileriYazdir()
#print("Yaşım:", kisi1.YasiDondur())
#del kisi1 # kisi1 isimli nesneyi siliyor.  Bir daha kullanmak istersek hata alırız
#print(kisi1.BilgileriYazdir())




#kisi2=Kisi("aslı","çelik",40)
#print("Yaş:", kisi2.YasiDondur())
#kisi2.yas=46
#print("Yaş:", kisi2.YasiDondur())
##del kisi2.yas # kisi2 nesnesindeki yas propertisini (özelliğini) siliyor.yas kullanılmak istenirse hata olur
##print("Yaş:", kisi2.YasiDondur())




#Hesaplayici adında bir sınıf oluşturunuz
#Bu sınıfta Topla,Cikart,Carp ve Bol adında geriye sonucu döndüren fonksiyonlar
#yazınız
class Hesaplayici:
    def Topla(self, sayi1,sayi2):
        return sayi1 + sayi2

    def Cikart(self, sayi1,sayi2):
        return sayi1 - sayi2

    def Carp(self, sayi1,sayi2):
        return sayi1 * sayi2

    def Bol(self,sayi1,sayi2):
        return sayi1 / sayi2

    def CokluTopla(self, *sayilar):
        return(sum(sayilar))



islem=Hesaplayici()
#print("Toplama:",islem.Topla(9,5))
#print("Çıkartma:",islem.Cikart(9,5))
#print("Çarpma:", islem.Carp(9,5))
#print("Bölme:", islem.Bol(9,5))
print(islem.CokluTopla(14,37))
print(islem.CokluTopla(30,4,26))
print(islem.CokluTopla(54,81,23,45,67,90,24))