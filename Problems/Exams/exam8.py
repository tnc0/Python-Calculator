def VizeDigitalSaat(Saat,Dakika,Saniye):
    Liste1 = []
    Liste2 = []
    for i in range(5):
        Liste1.append(str(Saat)+'.'+str(Dakika)+'.'+str(Saniye))
        Liste2.append([Saat,Dakika,Saniye])
        Saniye += 1
        if Saniye == 60:
            Saniye = 0
            Dakika += 1
        if Dakika == 60:
            Dakika = 0
            Saat += 1
        if Saat == 24:
            Saat = 0       
    return Liste1,Liste2
    
def VizeListeyiOlustur(baslangic,bitis):
    Liste = []
    for i in range(baslangic,bitis+1):
        if i%3==0:
            Liste.append(i)
    return Liste

def VizeRasgeleSayiliListeUret(baslangic,bitis,adet):
    import random
    Liste=[]
    for i in range(adet):
        sayi = round(random.random()*(bitis-baslangic)+baslangic)
        Liste.append(sayi)
    return Liste

def VizeSeriUret():
    Liste = []    
    for i in range(8):    
        Liste.append(i**2 - 1)
    return Liste

def VizeYerDegis(Liste):
    for i in range(0,len(Liste)-1,2):
        tmp = Liste[i]
        Liste[i]=Liste[i+1]
        Liste[i+1]=tmp
    return Liste

def VizeBozanElamanIndeksi(Liste):
    fark1 = []
    fark2 = []
    for i in range(1,len(Liste)):
        fark1.append(Liste[i]-Liste[i-1])
    for i in range(1,len(fark1)):
        fark2.append(fark1[i]-fark1[i-1])        
    indeks = 1
    for i in fark2:    
        if i!=0:
            break
        indeks+=1
        
    return indeks+2

def VizeBasVeSonHarfiBuyut(cumle):
    def HarfIseBuyut(s):
        if ord(s)>=ord('a') and ord(s)<=ord('z'):
            return chr(ord(s)-ord('a')+ord('A'))
        else:
            return s
    yeniCumle=''
    for i in range(len(cumle)):
        if (i==0) or (i==len(cumle)-1): # ilk veya son karakterse            
            yeniCumle+=HarfIseBuyut(cumle[i])
        else: 
            if (cumle[i+1]==' ' or cumle[i-1]==' '): # kelime başı veya sonu
                yeniCumle+=HarfIseBuyut(cumle[i])
            else:
                yeniCumle+=cumle[i]
                    
    return yeniCumle