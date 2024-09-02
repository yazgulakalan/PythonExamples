print("merhaba")
#python girilen 2 sayının toplamı 
sayi1=int(input("1. sayı : "))
sayi2=int(input("2. sayı : "))
toplam=sayi1+sayi2
print("girilen sayıların toplamı : ",toplam)
sayi1=float(input("1. sayı : "))
sayi2=float(input("2. sayı : "))
ortalama=(sayi1+sayi2)/2;
print("girilen sayıların ortalaması : ",ortalama)
not1=float(input("1. yazılı :"))
not2=float(input("2. yazılı :"))
ortalama=(not1+not2)/2
print("ortalamanız : ",ortalama)
if(ortalama<50):
    print("kaldınız :(")
else:
    print("tebrikler. geçtiniz")
sayi=int(input("Bir sayı girin : "))
if(sayi%2==0):
    print("Sayı Çift")
else:
    print("Sayı Tek")    
sayi=int(input("sayıyı girin : "))
if(sayi<0):
    print("sayı negatif")
elif(sayi>0):
    print("sayı pozitif")
else:
    print("sayı sıfırdır")   
sayi =1234

carpim=1
for rakam in str(sayi):

    carpim*=int(rakam)

print("Rakamları Çarpımı:",carpim)
sayi =1234

toplam=0

for rakam in str(sayi):
    toplam+= int(rakam)

    print("Rakamları toplamı:",toplam)
sayi = float(input("Bir sayi girin:"))

if sayi < 0:
    sayi*=-1

    print("Sayının mutlak değeri:",sayi)
for i in range(10):
    print("merhaba dünya")    
sayac=0
while sayac <10:
    sayac=sayac+1
    print("merhaba dünya")
print("merhaba dünya\n"*10)
isim = input("Bir isim girin:")
print(isim)    
isim = input("Bir isim girin:")

for i in range(10):
    print(isim)    
    
toplam =0
while True:
    sayi = int(input("Bir sayı girin:"))
    if sayi == 0:
        break
    toplam+=sayi

    print("Sayıların toplamı:",toplam)  
    liste=[10,20,30,40,50]
    toplam=0

    for sayi in liste:
        toplam+=sayi
        #toplam=toplam+sayi

        print("dizi elemanlarının toplamı : ",toplam)  
sayilar=[]

while True:
    sayi=int(input("Bir sayı girin:"))
    if sayi == 0:
        break
    sayilar.append(sayi)

toplam =sum(sayilar)
adet =len(sayilar)

print("Sayıların ortalaması:",toplam/adet)
isimler = []

for i in range(5):
    isimler.append(input("Bir isim girin:"))
for isim in isimler:
    print(isim)    
liste=[10,20,30]

toplam=0
adet=len(liste)

for sayi in liste:
    toplam+=sayi

ortalama=toplam/adet
print("Sayıların Ortalaması : ",ortalama)   
vize=int(input("Vize Notu : "))
final=int(input("Final Notu : "))
puan=(vize*0.4)+(final*0.6)
print("Yıl sonu puanınız : ",puan)
if(puan>=50 and final>=50):
    print("Tebrikler. Geçtiniz.")
else:
    print("Kaldınız")

#formula
# Area: pi * r * r
# perimeter: 2 * pi * r
import math 

#PROGRAM
r= float(input("Input radius :"))

area = round( math.pi * r * r,2)
perimeter = round (math.pi * 2 * r,2) 

print("Area of circle :",area)
print("perimeter of Circle :",perimeter)