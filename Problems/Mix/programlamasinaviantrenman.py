"""
#1.soru
                
a = int(input("1.sayi:"))
b = int(input("2.sayi:"))

print(a+b)


#2.soru

I = int(input("Akım:"))
R = int(input("Direnç:"))

print("V=",I*R)


#3.soru

kisa = int(input("kisa kenar:"))
uzun = int(input("uzun kenar:"))

print("Alan=",kisa*uzun,"\nCevre=",2*(kisa+uzun))


#4.soru

pi = 3.14
r = int(input("yaricap:"))

print("cemberin alani:",pi*(r**2))


#5.soru

gun = int(input("gun sayisi:"))
print(gun//365,"yil",(gun//365)*12,"ay")



#6.soru

sayi = int(input("3 basamakli sayi:"))
yuz = sayi//100
onluk = sayi - yuz*100
on = onluk//10
birlik = onluk - on*10
terssayi = birlik*100 + on*10 + yuz
print(terssayi)

"""

"""
#7.soru
yuzluk = int(input("100'luk tabandaki not:"))
print("5'lik tabandaki not:",yuzluk/20)


#8.soru
fiyat = int(input("fiyat:"))
kdv = int(input("KDV:"))
print("Toplam Fiyat:",fiyat + (fiyat*(kdv/100)))

"""
print(6)

alis = int(input("alis fiyati:"))
vergi = int(input("vergi:"))
kar = int(input("kar:"))

satis = alis*((vergi + 100)/100) + alis*(kar/100)

print(satis)

"""
sayi = int(input("3 basamakli sayi:"))

yuz = sayi//100
on = sayi//10 - yuz*10
bir = sayi -yuz*100-on*10

print("yuzler:",yuz,"onlar",on,"birler:",bir)
"""


"""

A = int(input("A:"))
B = int(input("B:"))
print(A,B)
A,B=B,A
print(A,B)





n = int(input("n:"))
k = int(input("k:"))

print(k*((n*(n+1))/2))






ax = int(input("ax:"))
ay = int(input("ay:"))
bx = int(input("bx:"))
by = int(input("by:"))
cx = ax + bx
cy = ay + by

print(cx,",",cy)

"""





