
class Sekil:
    def __init__(self,pAd, pAlan, pCevre):
        self.Ad = pAd
        self.Alan = pAlan
        self.Cevre = pCevre

    
    def SekilAdiYazdir(self):
        print("Şekil Adı:", self.Ad)


    def __str__(self):   # c# daki tostring metodu gibi
        return super().__str__()

    def AlanYazdir():
        pass

    def CevreYazdir():
        pass


class Cokgen(Sekil):
    def __init__(self, pAd, pAlan, pCevre,pKenarSayisi):
        Sekil.__init__(self,pAd, pAlan, pCevre)
        self.KenarSayisi = pKenarSayisi

    def KenarSayisiYazdir(self):
        print("Kenar sayısı:", self.KenarSayisi)


class Kare(Cokgen):
    def __init__(self, pAd, pAlan, pCevre, pKenarSayisi,pKenarUzunluk):
        Cokgen.__init__(self,pAd, pAlan, pCevre, pKenarSayisi)
        self.KenarUzunluk = pKenarUzunluk

    def AlanYazdir(self):
        self.Alan = self.KenarUzunluk * self.KenarUzunluk
        print("Alan:",self.Alan)

    def CevreYazdir(self):
        self.Cevre = 4 * self.KenarUzunluk
        print("Çevre:",self.Cevre)

    def __str__(self):
        return str(self.KenarUzunluk) + "X" + str(self.KenarUzunluk) + " bir kare"


class DikDortgen(Cokgen):
    def __init__(self, pAd, pAlan, pCevre, pKenarSayisi,pKisaKenarUzunluk,pUzunKenarUzunluk):
        super().__init__(pAd, pAlan, pCevre, pKenarSayisi)
        self.KisaKenarUzunluk = pKisaKenarUzunluk
        self.UzunKenarUzunluk = pUzunKenarUzunluk

    def AlanYazdir(self):
        self.Alan = self.KisaKenarUzunluk * self.UzunKenarUzunluk
        print("Alan:",self.Alan)

    def CevreYazdir(self):
        self.Cevre = 2 * (self.KisaKenarUzunluk + self.UzunKenarUzunluk)
        print("Çevre:",self.Cevre)

    def __str__(self):
        return str(self.KisaKenarUzunluk) + "X" + str(self.UzunKenarUzunluk) + " bir dikdörtgen"


sekil1 = Kare("Kare",0,0,4,6)
print(sekil1)
sekil1.SekilAdiYazdir()
sekil1.KenarSayisiYazdir()
sekil1.AlanYazdir()
sekil1.CevreYazdir()



sekil2 = DikDortgen("Dikdörtgen",0,0,4,5,12)
print(sekil2)
sekil2.SekilAdiYazdir()
sekil2.KenarSayisiYazdir()
sekil2.AlanYazdir()
sekil2.CevreYazdir()
