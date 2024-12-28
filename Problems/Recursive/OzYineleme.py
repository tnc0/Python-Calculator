def fun(n):
    if(n == 0):
        return
    fun(n//2)
    print(n%2,end="")

def fun(a):
    if(a == 0):
        return
    fun(a-1)
    print(a,end=" ")



def ortalama(x):
    ort = 0
    ortalama(x-1)
    for i in range(x):
        ort += int(input(f"{i+1}.sayi:")) 
    return ort/x


liste = []

def f(N):
    if(N == 0):
        return
    f(N-1)
    if(N%2 != 0):
        liste.append(N)
    return liste






def f(x, ort = 0):
    for i in range(x):
        ort += int(input("sayi:"))
    return ort/x





"""

liste = [11,11,2]
tekrarliste = []#2,2,1
yeniliste = []
for i in liste:
    tekrar = 0
    for j in liste:
        if(i == j):
            tekrar += 1
    tekrarliste.append(tekrar)

maks = tekrarliste[0]
for i in tekrarliste:
    if(i > maks):
        maks = i
print(maks)
max1 = liste[0]

for i in liste:
    if(i == max1):
        i = ""
        yeniliste.append(i)
    else:
        yeniliste.append(i)
print(yeniliste)

"""



def fibo(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(7))


def faktoriyel(n):
    if(n == 0):
        return 1
    return n*faktoriyel(n-1)
print(faktoriyel(5))


#Bir dizinin elemanlarının toplamını hesaplayan özyinelemeli bir Python fonksiyonu yazın.
# Kullanıcıdan bir dizi alın ve bu dizinin elemanlarının toplamını ekrana yazdırın.

def dizi(dizi1 = [1,2,3], kontrol = -1, top = 0):
    if(kontrol == len(dizi1)):
        return
    kontrol += 1
    return top + dizi(dizi1[kontrol])






