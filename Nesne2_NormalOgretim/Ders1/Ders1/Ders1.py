
#metin="Isparta uygulamalı bilimler üniversitesi"
#print(metin)
#print(metin[0])
#print(metin[5])
#print(metin[2:6]) #2.  indeksten 6.  indekse kadar yaz (6.  indeks dahil
#değil)


#yazi="murat"
#print(yazi.upper()) #hepsini büyük yapar


#digeryazi="OKUL"
#print(digeryazi.lower()) #hepsini küçük yapar



#metin="Bugün günlerden salı"
#print(metin.replace("salı","çarşamba")) #salı yı çarşamba olarak değiştirir


#meyveler="elma,armut,kiraz,nar,karpuz,ayva"
#print(meyveler)
#meyveListem=meyveler.split(',')
#print(meyveListem)



#yazim = "Bugün okula Ali gitti.  Fatma ise okula gitmedi."
##varmi = "Ali" in yazim # yazi nın içinde Ali varsa True, yoksa False döner
##varmi = "Ahmet" in yazim #false döner çünkü ahmet yazının içinde yok
#varmi = "Ahmet" not in yazim #true döner çünkü ahmet yazının içinde yok
#print(varmi)



#miktar = 5
#urun = "elma"
#fiyat = 3
#yazi = "Bugün pazardan {}KG {} yı {}TL den aldım"
#print(yazi.format(miktar,urun,fiyat))
#print(yazi.format(4,"muz",7))


#yazi1="bu bir yazı"
#yazi2='bu da bir diğer yazı'


#print('Bu Ali\'nin kitabı') # \ slash karakteri kaçış(escape) karakteri. Kendinden sonrakini yazdırır

#print("Dosya konumu C:\\")


#metin="Bilgisayar"
#print("yazı uzunluğu=", len(metin)) # len  karakter sayısı yani metin uzunluğunu verir


##yazi="189"  #true döndürür
#yazi="189?%+,,.W"  #false döndürür
#print(yazi.isalnum()) # yazı alfanumerikse yani içinde sadece rakamlar varsa True, değilse False döner




##yazi="murat" #True döner sadece karakter var
#yazi="murat45436"
#print(yazi.isalpha()) # yazı karakterlerden oluşuyorsa True, sayı varsa False



yazi="314"
print(yazi.isdecimal()) # içinde sadece sayı varsa True, başka karakterde varsa False