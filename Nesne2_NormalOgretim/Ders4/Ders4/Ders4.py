# list sıralıdır, eleman sayısı değişebilir, aynı elemanları içerebilir yani eleman tekrarı vardır. []
# tuple sıralıdır, eleman sayısı değişmez, aynı elemanları içerebilir. ()
# set sırasızdır, aynı elemanı içermez
# dict (dictionary) sırasız,  eleman sayısı değişebilir, aynı elemanı içermez


#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#print(type(meyveListem))
#print(len(meyveListem))
#print(meyveListem[2]) # 2. indeksteki elemanı yani örnekte kayısı yazar
#print(meyveListem[-1]) # sağ dan -1 indekste çilek olduğu için çilek yazar
#print(meyveListem[3:5]) #3. indeksten 5. indekse kadar al (5. indeks dahil değil)
#print(meyveListem[:4]) # başlangıçta bir sayı yoksa her zaman 0. indeksten yani en baştan başlar. 4. indekse kadar
#print(meyveListem[3:]) # başlangıç verilip son indeks verilmezse başlangıçtan itibaren hepsini alır
#print(meyveListem[-4:-1]) # -4. indeksten -1. indekse kadar(-1. indeks dahil değil)


#print(meyveListem)
#meyveListem[2]="muz" # listedeki 2. indeksteki elemana muz ata. yani 2. indeks artık muz oluyor
#print(meyveListem)

#for meyve in meyveListem:
#    print(meyve)



#for meyve in meyveListem:
#    if "i" in meyve:  # meyve i harfini içeriyorsa
#        print(meyve)



## listenin içinde e harfini içeren meyveleri başka listeye oluştur
#e_iceren_MeyveListem=[]
#for meyve in meyveListem:
#    if "e" in meyve:
#        e_iceren_MeyveListem.append(meyve) # append bir listeye eleman eklemek için kullanılır
#print(e_iceren_MeyveListem)




#u_iceren_MeyveListem=[meyve for meyve in meyveListem if "u" in meyve]
#print(u_iceren_MeyveListem)




#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#meyveListem.insert(4,"şeftali") # belirtilen indekse yani 4. indekse "şeftali" yerleştirir
#print(meyveListem)






#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#if "nar" in meyveListem:
#    meyveListem.remove("nar")  # eğer listede "nar" varsa listeden sil. Remove silme yapar
#print(meyveListem)






#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#meyveListem.pop() # listedeki son elemanı siler
#print(meyveListem)
#meyveListem.pop() # listedeki son elemanı siler
#print(meyveListem)






#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#del meyveListem[5] # 5. indeksteki elemanı siler
#print(meyveListem)





#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#meyveListem.clear() # clear listedeki tüm elemanları siler, yani listeyi temizler
#print(meyveListem)





#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#del meyveListem # del listeyi komple siler. Bundan sonra meyveListem değişkeni kullanılmak istenirse hata oluşur
##print(meyveListem) # yukarıda liste silindiği için yazdırılmaya çalışılırsa hata oluşur





#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#ikinciListem=meyveListem.copy()
#print(ikinciListem)





#listem1=["ali","mehmet","mine","aslı"]
#listem2=[41,65,875,2,6783,123,10]
#listem3=listem1+listem2
#print(listem3)





#listem1=["ali","mehmet","mine","aslı"]
#listem2=[41,65,875,2,6783,123,10]
#listem1.extend(listem2) # listem1 i listem2 ile genişletiyoruz, yani büyütüyor sonuna ekliyoruz
#print(listem1)






#tupleListesi=(532,46,4,1236,8,10)
#print(tupleListesi)
#print(type(tupleListesi))
#listListesi=list(tupleListesi) # list metodu tuple u list e dönüştürür
#print(listListesi)
#print(type(listListesi))





#sayiListem=[50,45,80,30,50,90,70,40,50,35,25,10,85,50,60]
#print(sayiListem.count(50)) # sayiListesinde kaç tane 50 varsa onun sayısını verir. örnek te 4 tane 50 olduğu için 4 yazar





#sayiListem=[50,45,80,30,50,90,70,40,50,35,25,10,85,50,60]
#print(sayiListem)
#sayiListem.sort() # küçükten büyüğe sıralı hale getirir
#print("küçükten büyüğe sıralı=",sayiListem)
#sayiListem.reverse() # listeyi ters çevirir
#print("büyükten küçüğe sıralı=",sayiListem)





#meyveListem=["elma","armut","kayısı","kiraz","erik","nar","üzüm","çilek"]
#print(meyveListem)
#meyveListem.sort() # küçükten büyüğe sıralı hale getirir
#print("alfabetik sıralı=",meyveListem)
#meyveListem.reverse() # listeyi ters çevirir
#print("ters alfabetik sıralı=",meyveListem)





tupleIsimListesi=("merve","fatih","kadir","zeynep",546,75475,True,'M',43.54745)
print(tupleIsimListesi)




