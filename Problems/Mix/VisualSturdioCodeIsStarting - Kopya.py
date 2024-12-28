
"""
c = input("bir cumle giriniz lutfen:")
sayac = 1
for i in c:
    if(i == " "):
        sayac += 1

print(sayac)
    """
"""
# İki farklı değere sahip iki liste oluşturun
liste1 = [1, 2, 3, 4, 5]
liste2 = [2, 4, 1, 5, 7]

# Ortalama değerlerini hesaplayın
ortalama1 = sum(liste1) / len(liste1)
ortalama2 = sum(liste2) / len(liste2)

# Korelasyon katsayısını hesaplayın
korelasyon_katsayisi = sum((x - ortalama1) * (y - ortalama2) for x, y in zip(liste1, liste2)) / \
                      (sum((x - ortalama1)**2 for x in liste1) * sum((y - ortalama2)**2 for y in liste2))**0.5

# Sonucu yazdırın
print("Korelasyon Katsayısı:", korelasyon_katsayisi)


    """

#Elemanları sıralayan program?
"""
liste = [1,2,3,4,5]
 
for sirala in liste:
    print(sirala)
    """

#Her elemanın tekrar sayısını bulan program?
"""
liste = [1,2,2,3,4,5]

tekrar_sayilari = {} #bir sözlük oluşturuldu.
for eleman in liste:
    if eleman in tekrar_sayilari:
        tekrar_sayilari[eleman] += 1
    else:
        tekrar_sayilari[eleman] = 1

for eleman, tekrar_sayisi in tekrar_sayilari.items():
    print(f"{eleman}: {tekrar_sayisi} kere tekrar ediyor.")
    """ 




#Girilen yazıdaki boşluk karakter sayısını bulan program?
"""
metin = input("icindeki bosluk sayisini görmek icin birden fazla kelimeli bir cumle yaziniz\n")
bosluksayac = 0
kelimesayac=1
for i in metin:
    if (i == " "):
        bosluksayac+=1
        kelimesayac+=1
print(f"cumlede{bosluksayac}tane bosluk var.")
print(f"cumlede{kelimesayac}tane kelime var.")
    """



#Girilen iki yazıyı karşılaştıran (eşit olup olmadığını bulan) program?
"""
metin1 = input("Lutfen 1. metninizi giriniz\n")
metin2 = input("Lutfen 2. metninizi giriniz\n")

l1 = []
l2 = []

for i in metin1:
    l1.append(i)
for t in metin2:
    l2.append(t)

if(l1 == l2):
    print("Cumleler ayni.")
else:
    print("cumleler farkli.")
    """
    


#Girilen yazının büyük yazılıp yazılmadığını bulan program?
"""
metin = input("Metni giriniz\n")

buyukmetin = metin.upper()
print(buyukmetin)
if(metin == buyukmetin):
    print("Girdiginiz metin buyuk harflerle yazilmistir.")
else:
    print("Girdiginiz metinde kucuk harf vardır.")
    """


#girilen metni "r" den "k" ya kadar yazdırmak.
"""
metin = input("Metin:\n")
k = int(input("(0'dan başlar.)hangi harften itibaren başlayacaksın?\n"))
r = int(input("(0'dan başlar.)hangi harfe kadar yazdıracaksın?\n"))

if(k == 1):
    k = 0

print(metin[k:r])

    """

#Girilen yazıdaki kelime, rakam ve karakter sayısını bulan adam
"""
girilen = input("rakam ve harf içeren bir metin giriniz:\n")
lint = []
lstr = []
lchar = []

for i in girilen:
    if i.isdigit(): #isdigit metodu:sayı mı değil mi kontrol eder.
        lint.append(i)
        lchar.append(i)
    else:
        lstr.append(i)
        lchar.append(i)
print(f"{len(lint)}tane integer")
print(f"{len(lstr)}tane str")
print(f"{len(lchar)}tane character var")
    
    """
#Girilen yazıdaki aranan kelimenin önüne ve arkasına TIRNAK sembolünü ekleyen program?

"""
metin = input("birden çok kelimeli bir metin giriniz:\n")
k = input("hangi kelimeyi tırnak içine almak istersiniz:\n")

yenimetin = metin.replace(k,f'"{k}"')

print(yenimetin)

    """



#Girilen yazıdaki bir karakteri sil
#list.remove(object) = istenen objeyi siler
"""
alist = ["ben","sen"]

print(alist)
a = input("hangi nesneyi silmek istediğini seç")

alist.remove(a)

print(alist)
"""



#Girilen yazıdaki bir kelimeyi sil
"""
metin = input("birden çok kelimeli bir metin giriniz:\n")
k = input("hangi kelimeyi silmek istersiniz:\n")

yenimetin = metin.replace(k,"")

print(f"yeni metin: {yenimetin}")
    
    """


#Girilen yazıdaki noktalama işaretlerini sil
"""
metin = input("içinde noktalama işareti olan bir cümle giriniz:\n")
yenikelime=[]
noktalamalistesi = [",",".",":",";","?","-","_","!","'",]
for i in metin:
    if i not in noktalamalistesi:
        yenikelime.append(i)
for z in yenikelime:
    print(z,end="")
"""




#Girilen onluk tabandaki sayıyı ikilik tabandaki sayıya dönüştürünüz?
"""
a = int(input("onluk tabanda bir sayi giriniz:"))
sifrelistesi = []

while a > 0:
    kalan = a%2
    sifrelistesi.append(kalan)
    a = a // 2
print("girdiğiniz onluk tabandaki sayının ikilik tabandaki karşılığı aşağıda")
for i in sifrelistesi:
    print(i,end="")
    """


"""
a = int(input("1 den ona kadar bir sayi giriniz:"))

b = 0

while b<=9:
    b = b+1
    c = a*b
    print(f"{a}*{b}={c}")
    
    """


"""    
l = [12,50,75,145,150,180,525]

for i in l:
    if(i > 500):
        break
    if(i > 150):
        continue
    if(i%5 == 0):
        print(i)
    
    """


"""
dizi = [1,2,3,4,5,6,8,9]

sayac1 = -1

for i in dizi:
    sayac1 +=1
    if(sayac1%2 != 0):
        print(i)
"""

"""
a = 1
b = 0
print(a)
while (a<34):
    a,b=a+b,a
    print(a)
    
    """



#10 TANE BALON
"""
l = [10,20,30,40,50,60,70,80,90]
lson = []

sayac =2
for i in l:                                 #[30,60,90,40,80,50,20,70]
    lson.append(l[sayac])
    l.remove(l[sayac])
    sayac += 2
    if(sayac > 9):
        sayac = 2
print(lson)
    
    """

    

#Girilen onluk sayıyı onaltılık sayıya dönüştürünüz?

"""
a = input("onluk tabanda bir sayi giriniz\n")

bol = int(a)//16
kalan = int(a)%16

if(bol == 0):
    bol = ""
if(kalan == 10):
    kalan = "A"
elif(kalan == 11):
    kalan = "B"
elif(kalan == 12):
    kalan = "C"
elif(kalan == 13):
    kalan = "D"
elif(kalan == 14):
    kalan = "E"
elif(kalan == 15):
    kalan = "F"

print(f"{bol}{kalan}")

    """


#Girilen ikilik sayıyı onluk sayıya dönüştürünüz?
"""
binary = input("ikilik tabanda bir sayi gir\n")
#binary = 10 --> ( 2**1*1 + 2**0*0 )=2
#binary[::-1] = 01
us = 0
toplam = 0
for i in binary[::-1]:
    toplam +=(2**us)*int(i)
    us += 1
print(toplam)

    """
"""
a = [[1,2,3,4],[1,2,3,5],[1,2,3,5],[1,2,3,5]]

for i in range(len(a)):# listenin içinde dolaşıyorum
    for p in range(len(a[i])):#listenin ilk elemanı olan listenin içinde dolaşıyorum
        print(a[i][p],end=" ")
    print() #alta geçmesini sağladım    
    """


