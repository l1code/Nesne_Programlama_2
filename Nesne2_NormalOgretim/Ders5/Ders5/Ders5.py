#girilenDeger=input("Lütfen bir yazı yaz ve enter a bas ")
#print("girdiğin yazı=", girilenDeger);



##klavyeden girilen iki tam sayının toplamı
#sayi1 = int(input("1.  sayıyı giriniz "))
#sayi2 = int(input("2.  sayıyı giriniz "))
#toplam = sayi1 + sayi2
#print("{0}+{1}={2}".format(sayi1,sayi2,toplam))




##klavyeden girilen iki ondalıklı sayının çarpımı
#sayi1 = float(input("1.  sayıyı giriniz "))
#sayi2 = float(input("2.  sayıyı giriniz "))
#carpim = sayi1 + sayi2
#print("{0}*{1}={2}".format(sayi1,sayi2,carpim))




##klavyeden girilen 5 sayıyı bir listeye doldurun.  Liste dolduktan sonra
##listenim en küçük, en büyük elemanını
## eleman toplamını ve ortalamasını bulunuz
#listem = []
#for x in range(1,6):
#    girilenSayi = int(input(str(x) + ". sayıyı giriniz: "))
#    listem.append(girilenSayi)


#toplam = sum(listem) # sum verilen çoklu eleman (liste ve diğerleri) toplamını verir
#print("Eleman toplamı=", toplam)
#print("Ortalama=", toplam / len(listem))

##en küçük ve en büyük eleman bulunurken sort edip buluyorduk
#print("En küçük eleman=", min(listem))
#print("En büyük eleman=",max(listem))





#benimTuple=(43,74,23,54,87,90,23,54,20,12)
##print(benimTuple[3]) # 3. indeksteki elemanı verir
##benimTuple[3]=100 # hata verir çünkü tuple ların eleman sayısı ve içeriği değişmez
## bir tupledaki eleman değiştirilmek isteniyorsa list e dönüştürülür sonra değişiklik yapılır
#print(benimTuple)
#listem=list(benimTuple)
#listem[3]=100
#benimTuple=tuple(listem) # tuple kendisine verilen değeri tuple a dönüştürür
#print(benimTuple)





#sayiTuple=(45,20,83)
#(sayi1,sayi2,sayi3)=sayiTuple
#print(sayi1)
#print(sayi2)
#print(sayi3)





#benimTuple=(44,24,75,24,76,44,78,26,7757,242,587,44,246,227)
##print("Eleman sayısı:", len(benimTuple))
##print("44 sayısı:", benimTuple.count(44))

#for x in benimTuple:
#    print(x)





#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#if("kavun" not in benimSet):
#    benimSet.add("kavun")
#print(benimSet)





#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.update(["kayısı","vişne","çilek","nar"])
#print(benimSet)






#benimSet={"elma","armut","kiraz","elma","kiraz","kiraz"} # aynı eleman çok sayıda olsa da sadece tek gibi olur
#print(benimSet)





#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.remove("armut") #belirtilen eleman set te varsa siler, yoksa hata verir.
#print(benimSet)

#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.remove("muz") #belirtilen eleman set te varsa siler, yoksa hata verir.
#print(benimSet)



#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.discard("elma") #belirtilen eleman set te varsa siler, yoksa hata vermez. hiçbirşey olmaz
#print(benimSet)




#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.discard("muz") #belirtilen eleman set te varsa siler, yoksa hata vermez. hiçbirşey olmaz
#print(benimSet)




#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#benimSet.clear() #set i temizler, elemanları siler
#print(benimSet)




#benimSet={"elma","armut","kiraz"}
#print(benimSet)
#del benimSet  # del set i komple siler. Sonraki satırlarda kullanmak istersek hata alırız
#print(benimSet)





#benimDict={"marka":"renault","model":"megane","yıl":2018}
#print(benimDict)
#print(benimDict["model"]) # verilen key(anahtar) e ait value(değer) yu döndürür
#print(benimDict.get("marka")) # verilen key(anahtar) e ait value(değer) yu döndürür
#benimDict["yıl"]=2021 # dict in değerini başka değerle değiştirebilirim
#print(benimDict)




#benimDict={"marka":"renault","model":"megane","yıl":2018}
##tüm key yani anahtarları yazdırma
#for x in benimDict:
#    print(x)


#tüm value yani değerleri yazdırma
#for x in benimDict.values():
#    print(x)


#tüm value yani değerleri yazdırma
#for x in benimDict:
#    print(benimDict[x])



#for x,y in benimDict.items():
#    print(str(x) +  ":" + str(y))





#benimDict={"marka":"renault","model":"megane","yıl":2018}
#print(benimDict)
#benimDict["renk"]="beyaz" #olmayan key verilirse bunu ekleme yapar
#print(benimDict)




#benimDict={"marka":"renault","model":"megane","yıl":2018}
#print(benimDict)
#del benimDict["model"] # belirtilen key ve value yu siler
#print(benimDict)




#aile={
#    "cocuk1":{"ad":"mert","dogumYılı":2004},
#    "cocuk2":{"ad":"beyza","dogumYılı":2011},
#    "cocuk3":{"ad":"fatih","dogumYılı":2018}
#    }


##print(aile)
#print(aile["cocuk2"])





kisiDict=dict(ad="murat",soyad="ince",TCNO=64754865432, dogumYili=1985,dogumYeri="antalya")
#print(kisiDict)
print(kisiDict["TCNO"])