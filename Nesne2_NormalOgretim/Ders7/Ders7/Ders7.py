
#def SayiyaBesEkle(x):
#    return x+5

#print(SayiyaBesEkle(100))


#SayiyaBesEkle=lambda x:x+5
#print(SayiyaBesEkle(100))
#print(SayiyaBesEkle(20))



##iki sayının toplamını bulan lambda ifadesi
#topla=lambda sayi1,sayi2: sayi1+sayi2
#print(topla(15,50))



## üst alma lambda ifadesi
#ustKuvvetHesapla=lambda taban,ustKuvvet:taban**ustKuvvet
#print(ustKuvvetHesapla(2,3)) # 2*2*2=8 demek
#print(ustKuvvetHesapla(5,4)) # 5*5*5*5=625 demek




#def BenimFonksiyonum(n):
#    return lambda a:a*n

#ikiyleCarpan=BenimFonksiyonum(2)
#print(ikiyleCarpan(5))

#ucleCarpan=BenimFonksiyonum(3)
#print(ucleCarpan(5))




#karakter=chr(65)  # 65 ascii de büyük A nın sayısal değeri
#print(karakter)
#print(chr(213))
#print(chr(247))





#x="print('merhaba')"
#eval(x)  # evaluate kısaltması. kendiisne verilen python kodunu çalıştırır




#kodum='print(5+3)'
#eval(kodum)



#baskaKod='35-10'
#print(eval(baskaKod))





#for i in range(1,11):
#    print(i)


#kodSatiri='for i in range(1,11):\n\tprint(i)'
#exec(kodSatiri)  #exec execute kısaltması yani çalıştır demek. kendisine verilen kod bloku çalıştırır




#print(abs(-300))  # 300 yazar. abs mutlak değeri verir. sonuç pozitif çıkar


#print(pow(4,3))  # 4 üsü 3 yapar yani 4*4*4=64 yazar



#print(round(3.689321)) # 4 yazar. Eğer ikinci parametre girilmezde noktadan(virgülden) sonraki rakama göre yuvarla
#print(round(3.2689321)) # 3 yazar.
#print(round(8.689721,3)) # 8.69 yazar. noktadan(virgülden) sonra 3 basamaka kadar yuvarla




# a) klavyeden girilen python kod parçasını çalıştıran  bir fonksiyon yazınız
# b) a şıkkında hazırladığınız fonksiyona klavyeden girilen iki sayının toplamını bulan kodu gönder

def PythonKoduCalistir(pythonKodu):
    exec(pythonKodu)


girilenKod=input("Lütfen çalıştırmak istediğiniz python kodunuz yazınız:\n")
calistirilacakKod=girilenKod.replace('\\n','\n')
PythonKoduCalistir(calistirilacakKod)

