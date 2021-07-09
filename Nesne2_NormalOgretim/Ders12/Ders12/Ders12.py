
#import threading

#def Fonksiyonum():
#    print("Fonksiyon çağrılma sayısı")


#timer=threading.Timer(3,Fonksiyonum)
#timer.start()

#timer.cancel()




#import time as t
#zaman=10
#for i in range(zaman):
#    print(str(zaman-i) + " saniye kaldı")
#    t.sleep(1) # 1 saniyelik duraklat

#print("Süre bitti !!!")






## her 5 saniyede rastgele bir sayı oluşturup bu sayıları bir dosyaya alt alta kaydeden kodlar
#import time
#import random
#sayac=0
#while True:
#    sayac+=1
#    f=open("dosyam.txt","a")
#    rastgeleSayi=random.randint(1,100)
#    f.write(str(rastgeleSayi) + "\n")
#    f.close()
#    print(str(sayac) + " .  sayı üretildi ve dosyaya kaydedildi")
#    time.sleep(5) # 5 saniye uyu yani durakla demek
#    if sayac==12: # sayacın 12 olması demek 12*5=60 sn yani 1dk demek.  1dk
#    sonra işlemi durdurmak için
#        break

#print("Sayı üretme ve dosyaya kaydetme işlemi bitti !!!")








def CagrilacakFonksiyon(kacDefa):
    print(kacDefa, " . defa çağrıldım")


import time
sayac = 0
while True:
    sayac+=1
    CagrilacakFonksiyon(sayac)
    time.sleep(2) #2 saniyede bir
    if sayac == 10:
        break

print("Fonksiyon çağırma işlemi bitti !!!!!")

