def RastgeleSayiliListeUret(baslangic,bitis,adet):
    sayiliste = []
    import random
    while True:
        if len(sayiliste) == 10:
            break
        x = (random.random() * 3 + 5) 
        if baslangic < int(x) < bitis:
            sayiliste.append(int(x))
        
    return sayiliste
print(RastgeleSayiliListeUret(5,8,10))

import random

def RasgeleSayiliListeUret(baslangic, bitis, adet):

    Liste = []
    for i in range(adet):
        a = random.random()
        x = (random.random() * 3 + 5) 
        
        if baslangic < int(x) < bitis:
            Liste.append(int(x))
    return Liste

print(RasgeleSayiliListeUret(5, 8, 10))
#1.soru


def DigitalSaat(saat,dakika,saniye):
    Liste = []
    for i in range(5):
        Liste.append(saat)
        Liste.append(dakika)
        Liste.append(saniye)
        saniye += 1
        if(saniye == 60):
            dakika += 1
            saniye = 0
            if(dakika == 60):
                saat +=1
                dakika = 0
                if(saat == 24):
                    saat = 0
    return Liste
print(DigitalSaat(18,20,58))


#+2.soru


def ListeyiOlustur(baslangic,bitis):
    Liste=[]
    for i in range(baslangic,bitis+1):
        if(i%3 == 0):
            Liste.append(i)
    return Liste

#3.soru
import random
def RasgeleSayiliListeUret(baslangic,bitis,adet):
    Liste = []
    for i in range(adet):
        a = random.random()
        a = round(a)
        Liste.append(a)
    return Liste

print(RasgeleSayiliListeUret(5,8,10))

#4.soru
Liste = [1,2,3,4,5,6,7,8,9,10]
def YerDegis(Liste):
    a = 0
    b = 1
    c = 5
    for i in range(c):
        Liste[a],Liste[b] = Liste[b],Liste[a]
        
        a +=2
        b +=2
    return Liste
print(YerDegis(Liste))

#5.soru




#6.soru
Liste = [1,3,5,7,9,12,13]
def BozanElemanIndeksi(Liste):
    a = 0
    b = 1
    
    for i in range(6):
        if(Liste[b]-Liste[a] != 2):
            
            Indeks = Liste[b]
            break
        a +=1
        b+=1
    return Indeks
print(BozanElemanIndeksi(Liste))


        