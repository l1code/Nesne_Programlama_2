#class Kisi:
#    def __init__(self, pAd,pSoyad):
#        self.Ad=pAd
#        self.Soyad=pSoyad

#    def BilgiYazdir(self):
#        print(self.Ad + " " + self.Soyad)


#k1=Kisi("Murat","İNCE")
#k1.BilgiYazdir()


#class Personel(Kisi):
#    def __init__(self, pAd, pSoyad,pSicilNo):
#        #Kisi.__init__(self,pAd,pSoyad)
#        super().__init__(pAd,pSoyad)
#        self.SicilNo=pSicilNo

    
#    def SicilNoYazdir(self):
#        print("Sicil No:", self.SicilNo)


#p1=Personel("Mehmet","Yıldırım","04389")
#p1.BilgiYazdir()
#p1.SicilNoYazdir()





## Hesaplama modülü kullanımı
#import Hesaplama
##Hesaplama.ToplamYaz(20,45)  # Hesaplama modülündeki fonksiyonu kullandık
#kisiBilgisi=Hesaplama.kisi1["ad"] + " " + Hesaplama.kisi1["soyad"]
#print(kisiBilgisi)


## Hesaplama modülünden kısmi import yani sadece belirli elemanı import etmek
#from Hesaplama import meyveListesi
#print(meyveListesi[4])


## modül adını kısaltma ya da değiştirme
#import Hesaplama as hs
#hs.ToplamYaz(34,40);



#import platform
#print(platform.system())
#print(dir(platform))
