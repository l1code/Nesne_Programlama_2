
#def BenimFonksiyonum():
#    print("Bu fonksiyon çalıştı!!!")

#BenimFonksiyonum()




#def ParametreAlanFonksiyon(p1):
#    print("Merhaba ", p1)

#ParametreAlanFonksiyon("murat")
#ParametreAlanFonksiyon("ebru")




# iki sayının toplamını bulan bir fonksiyon yazınız.  Klavyeden girilen iki
# sayının toplamını bu fonksiyonu kullanarak hesaplatıp ekrana yazdırınız

#def SayilarinToplaminiYaz(sayi1,sayi2):
#    print(sayi1+sayi2)


#def SayilarinToplaminiDondur(sayi1,sayi2):
#    return sayi1 + sayi2

#s1 = int(input("1.  sayıyı giriniz: "))
#s2 = int(input("2.  sayıyı giriniz: "))
##SayilarinToplaminiYaz(s1,s2)
#print(SayilarinToplaminiDondur(s1,s2))




## fonksiyonun kaç parametre alacağı belli değilse * konur
#def KisiAdlari(*isimler):
#    print("2.  kişinin adı:",isimler[1])


##KisiAdlari("ahmet","esra","mehmet","merve","elif");
#KisiAdlari("veli","aslı","mahmut")




## key value yani anahtar değer ikilisi olarakda fonksiyona parametre
## yollanabilir
#def KisiAdlari(kisi1,kisi2,kisi3):
#    print("3.  kişinin adı:",kisi3)

#KisiAdlari(kisi1="murat",kisi2="fatih",kisi3="mert")




#def KisiBilgileri(**Kisiler):
#    print("Adı:", Kisiler["Ad"])
#    print("Soyadı:", Kisiler["Soyad"])
#    print("Yaşı:",str(Kisiler["Yas"]))

#KisiBilgileri(Ad="murat",Soyad="ince",Yas=35)




##default yani varsayılan parametreli fonksiyon
#def BenimMemleketim(memleket="antalya"):
#    print("Memleketim", memleket)


#BenimMemleketim()
#BenimMemleketim("Burdur")





##bir fonklsiyon yazdığınızda içerisini sonra dolduracaksanız pass yazın yoksa
##hata alırsınız
#def BuBirFonksiyon():
#    pass

#BuBirFonksiyon()






# a) kendisine bir liste gönderilince listedeki en küçük elemanı döndüren bir
# fonksiyon yaz
# b) kendisine bir liste gönderilince listedeki en küçük elemanı döndüren bir
# fonksiyon yaz
# c) kendisine bir liste gönderilince listedeki eleman toplamını ve
# ortalamasını döndüren fonksiyon yaz
# d) rastgele 10 elemanlı bir liste oluştur ve içini 10-99(dahil) rastgele
# sayılarla doldur.  Bu listeyi
# a,b,c şıklarındaki fonksiyonlara gönder

def ListeninEnKucukElemani(listem):
    listem.sort()
    return(listem[0])


def ListeninEnBuyukElemani(listem):
    listem.sort()
    return(listem[len(listem) - 1])


def AyniAndaToplamVeOrtalamaDondur(listem):
    toplam = 0
    for x in listem:
        toplam+=x
    return toplam, toplam / len(listem)



import random
rastgeleListem=[]
for x in range(10):
    rastgeleSayi=random.randint(10,99)
    rastgeleListem.append(rastgeleSayi)
    print(rastgeleSayi)


print("En küçük eleman=", ListeninEnKucukElemani(rastgeleListem))
print("En büyük eleman=", ListeninEnBuyukElemani(rastgeleListem))
elemanToplami,listeOrtalamasi=AyniAndaToplamVeOrtalamaDondur(rastgeleListem)
print("Eleman toplamı=", elemanToplami)
print("Liste ortalaması=", listeOrtalamasi)






