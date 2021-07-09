
##x=int(3.2)
##x=int(4.7)
#x=int("8")
#print(x)
#print(type(x))




##y=float(7)
#y=float("12.64")
#print(y)
#print(type(y))




##z=str(4)
#z=str(6.18)
#print(z)
#print(type(z))




#a=5
#b=3
#c=4
##toplam=a+b+c
#print(toplam)
#fark=a-b
#print(fark)

#islem=a*b
#print(islem) # 15 yazar

#islem=a**b # a üssü b işlemi yani örnekte 5 üssü 3 hesaplar 5*5*5=125 yazar
#print(islem)




#islem=10/4 #normal bölme işlemi
#print(islem)

#islem=10//4 #bölümün tam kısmını verir.  10 un 4 e 2.5 yapar fakat tam kısmı
#nı yani 2 yazar
#islem=48//7 # 6 yazar çünkü 48 in 7 ye bölümünden kalan 6.XXXX gibi bir sayı.
#tam kısmı 6 yı alır
#print(islem)


#islem=10%3 # mod (bölümden kalanı verir) 10 un 3 e bölümünden kalan 1 dir
#print(islem)



#x=4
#x+=2 # x=x+2 demek
#print(x) # 6 yazar
#x*=3 # x=x*3
#print(x) # x 6 olduğu için 6*3=18 yazar



#print(5>3) # Doğru ifade olduğu için True yazar
#print(6<20) #Doğru ifade olduğu için True yazar
#print(100>=300) #Yanlış bir ifade olduğu için False yazar


#aşağıdaki ifadelerde hep True yazar çünkü dolular
#print(bool(324))
#print(bool("okul"))
#meyveler=["elma","armut","kayısı"]
#print(bool(meyveler))


#aşağıdaki ifadelerde hep False yazar çünkü boşlar
#print(bool(0))
#print(bool(None))
#metin=""
#print(bool(metin)) #metin yani string ifade boş ise False yazar
#bosliste=[]
#print(bool(bosliste)) # boş liste False yazar



#x = [10,20]
#y = [10,20]
#z = x # x ve z aynı eleman olmuş oluyor
##print(x is y) # x y dir diyor fakat x y değildir.  Sadece değerleri eşittir.
##Bu sebeple False yazar
##print(x is z) # x z dir diyor.  Doğru bir ifade çünkü z=x yaparak birbirine
##aynı değişkeni atıyoruz.  True yazar
##print(10 in x) # 10 x in içinde vardır diyor.  10 x in içinde olduğu için
##True döner
#print(40 in x) # 40 x in içinde vardır diyor.  40 x in içinde olmadığı için
#False döner



#x = 6
#print(x >= 4 and x <= 10) # x in değeri bu aralık yani 6 olduğu için True
#döner



#x = 50
#print(x >= 4 and x <= 10) # x in değeri bu aralıkta olmadığı yani 50 olduğu
#için False döner



#x = 20
#print(x >= 15 or x < 9) # koşulun bir tanesi bile doğru olsa True döner


#ogrenciNotu = 700 
#if(not(ogrenciNotu >= 0 and ogrenciNotu <= 100)):
#    print("Lütfen 0-100 aralığında not giriniz")




import random
#print(random.randrange(1,10)) # 1 ve 9 dahil rastgele sayı üretir. Üst sınır olan 10 u üretmez
#print(random.randrange(1,11)) # 1 ve 10 dahil rastgele sayı üretir.

#print(random.random()) # ondalıklı sayı üretir
#print(random.randint(1,5)) # 1 ve 5 dahil rastgele sayı üretir. Yani başlangıç ve bitiş sayıları dahil



random.seed(50) #zamanlayıcının hep aynı sayı üretmesini sağlar
print(random.random())

random.seed(75) #zamanlayıcının hep aynı sayı üretmesini sağlar
print(random.random())