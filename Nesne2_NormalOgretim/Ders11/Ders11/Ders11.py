
#dosya=open("metinDosyasi.txt","w") # w write kısaltması. Her çalıştığında dosya içerisindeki eski veri silinir
##dosya.write("ben ilk satırım")
#dosya.write("ben yeni yazıyım")
#dosya.close()



#eklemeliDosya=open("eklemeliMetinDosyasi.txt","a") # a append kısaltması ekleme yapar
##eklemeliDosya.write("ben 1. satırım")
##eklemeliDosya.write("\nben 2. satırım")
#eklemeliDosya.write("\nben diğer bir eklenen satırım")
#eklemeliDosya.close()




#dosyaOku=open("eklemeliMetinDosyasi.txt","r") # r read kısaltması
#okunanVeri=dosyaOku.read() # tüm dosya içeriğini tek seferde okur
#print(okunanVeri)




#dosyaOku=open("eklemeliMetinDosyasi.txt","r") 
#okunanSatir=dosyaOku.readline() # readline her çağırıldığında bir satır okur
#print(okunanSatir)
#okunanSatir=dosyaOku.readline() # readline her çağırıldığında bir satır okur
#print(okunanSatir)


#dosyaOku=open("eklemeliMetinDosyasi.txt","r") 
#okunanKarakterler=dosyaOku.read(7) # belirtilen sayı kadar yani 7 karakter okur
#print(okunanKarakterler)




##dosya silme işlemi
#import os
#os.remove("silinecekDosya.txt")




##dosya var mı yok mu
#import os
#if os.path.exists("eklemeliMetinDosyasi.txt"):
#    print("Dosya mevcut")
#else:
#    print("Böyle bir dosya yok")




#farkliKonumDosya=open("C:\\Users\\muratince\\Desktop\\ders11\\farkliKonumdakiDosya.txt","w") # w write kısaltması. Her çalıştığında dosya içerisindeki eski veri silinir
#farkliKonumDosya.write("ben farklı konumdaki dosyadaki yazıyım")
#farkliKonumDosya.close()




#import os
#klasorIcindekiler=os.listdir("C:\\Users\\muratince\\Desktop\\2021 Bahar Dersler")
#for x in klasorIcindekiler:
#    print(x)



#import os #dolu klasör silinemez. Silmek için içerisindekilerin silinmesi gerekir
#os.rmdir("C:\\Users\\muratince\\Desktop\\ders11")






import datetime
#def convert_to_date(timeStamp): #zaman damgası olarak parametre alan fonksiyon
#    d=datetime.datetime.utcfromtimestamp(timeStamp)
#    formattedDate=d.strftime("%d %b %Y")
#    return formattedDate



#import os
#with os.scandir("C:\\Users\\muratince\\Desktop\\2021 Bahar Dersler") as klasorDetayBilgiler:
#    for x in klasorDetayBilgiler:
#        print("Adı:",x.name)
#        print("Boyutu:",x.stat().st_size) # byte cinsinden boyut döndürür
#        #print("Oluşturulma zamanı:",x.stat().st_ctime) # create time yani oluşturulma zamanı fakat zaman damgası şeklinde
#        #print("Değiştirilme zamanı:",x.stat().st_mtime) # modified time yani değiştirilme zamanı fakat zaman damgası şeklinde
#        print("Oluşturulma zamanı:",convert_to_date(x.stat().st_ctime)) 
#        print("Değiştirilme zamanı:",convert_to_date(x.stat().st_mtime))





#import os
#os.mkdir("benYeniKlasorum")  # tek klasör oluşturma
#os.makedirs("2021/6/15")  # hiyerarşik yani içi içe dallanmış şekilde klasörler

