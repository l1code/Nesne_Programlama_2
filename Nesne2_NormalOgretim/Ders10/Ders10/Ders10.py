
import datetime

#mevcutTarih = datetime.datetime.now()
#print(mevcutTarih)
#print(mevcutTarih.year)
#print(mevcutTarih.month)
#print(mevcutTarih.day)
#print(mevcutTarih.hour)
#print(mevcutTarih.strftime("%A")) # gün adını yazar



tarih = datetime.datetime(2021,6,20,18,45,33)  # 20 Haziran 2021 saat 18:45:33
#print(tarih.strftime("%A")) # gün adını tam yazar
#print(tarih.strftime("%a")) # gün adını kısa yazar
#print(tarih.strftime("%B")) # ayın adını tam yazar
#print(tarih.strftime("%b")) # ayın adını kısa yazar
#print(tarih.strftime("%w")) # haftanın kaçıncı günü olduğunu verir. Pazar günü 0. gün
#print(tarih.strftime("%d")) # ayın kaçıncı günü olduğunu verir
#print(tarih.strftime("%m")) # yılın kaçıncı ayı olduğunu verir
#print(tarih.strftime("%Y")) # hangi yıl olduğunu verir
#print(tarih.strftime("%y")) # hangi yıl olduğunu son iki rakama göre verir
#print(tarih.strftime("%H")) # 00-24 formatına göre saati verir
#print(tarih.strftime("%I") + " " + tarih.strftime("%p")) # %I 00-12 formatına göre saat verir. %p ise am/pm verir
#print(tarih.strftime("%M"))  # dakikayı verir
#print(tarih.strftime("%S")) # saniye verir
##print(tarih.strftime("%c"))
#print(tarih.strftime("%x")) # local tarihe göre
#print(tarih.strftime("%X")) # local saate göre



#tarih2=datetime.datetime(2021,10,7)
#tarih1=datetime.datetime(2021,2,15)
#tarihFark=tarih2-tarih1
#print(tarihFark.days)





simdi=datetime.datetime.now()
print(simdi)
print(simdi.strftime("%c"))
import locale
locale.setlocale(locale.LC_ALL,'tr') # sistem bilgilerini tr ye dönüştürdük. Hangi dil istenirse tr yerine o yazılır
print(simdi.strftime("%c"))
print(simdi.strftime("%A"))
print(simdi.strftime("%B"))

