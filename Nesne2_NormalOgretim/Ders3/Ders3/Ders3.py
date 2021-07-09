
#metin = "tbmyo bilgisayar"
#i = 0
#while i < len(metin):
#    print(metin[i])
#    i+=1



#liste = ["elma","armut","portakal","ayva"]
#i = 0
#while i < len(liste):
#    print(liste[i])
#    i+=1



#i = 1
#while i <= 10:
#    print(i)
#    if i == 7:
#        break #döngüyü kırar
#    i+=1



#i = 0
#while i <= 10:
#    i+=1
#    if i % 2 == 1:
#        continue # alt satırdaki kodlar çalışmadan döngünün başına gidiyordu
#    print(i)




#listem = [2424,57,232,6,85434,532,21]
#for i in listem:
#    print(i)



#for i in range(10): # 0'dan 9'a kadar (0 ve 9 dahil) sayıları yazar.  10
#rakamı dahil değil
#    print(i)



#for i in range(1,11): #1 ve 10 dahil sayıları yazar.  başlangıç ve bitiş
#değeri verilebilir
#    print(i)



#for i in range (0,50,3): #0 dan başlayıp 50 ye kadar (dahil değil) sayıları 3
#er arttır
#    print(i)



#for i in "tbmyo bilgisayar":
#    print(i)




## 10 adet 1-100(dahil) rastgele sayı oluşturup alt alta yazdıralım.  Ayrıca en
## sonda toplamını yazdıralım
#import random
#toplam = 0
#for i in range(10):
#    rastgeleSayi = random.randint(1,100)
#    print(rastgeleSayi)
#    toplam+=rastgeleSayi
#print("Sayıların toplamı=",toplam)



#print("merhaba","nasılsınız",sep='-------') #iki string arasına sep de
#belirtilen yazıyı koyuyor


#print(*"okul",sep='\n') # verilen string karakterlerinin arasına sep de
#belirtilen karakteri koyar.

#print(*"okul",sep='*') # karakterler arasına yıldız koyar

#print(*"123456789",sep='-')


#print(*range(5)) # 0 dan 4 (dahil) e kadar sayıları yazdırır

#print(*range(3,12))

#print(*range(10,0,-1))



##yan yana yazdırmak için
#for i in range(1,11):
#    print(i,end="") # her bir karakter yazdırıldıktan sonra end parametresindeki ifade ona eklenir





