def ListeOlustur(m,a,b):
    import random
    Liste = []
    sayac = 0
    while(sayac < m):
        x = int((random.random())*10) 
        print(x)
        if(a <= x <= b):
            Liste.append(x)
            sayac += 1
    return Liste
print(ListeOlustur(5,3,8))


def Topla(Liste):
    m = len(Liste)
    a = 0
    if(m % 2 != 0):
        m += 1
    yeniliste = []
    for i in range(m/2):
        yeniliste.append(Liste[a] + Liste[m])     
        a += 1
        m -= 1
        if(a == m):
            yeniliste.append(Liste[a])
    return yeniliste



def BuyukHarf(cumle):
    sayi = 0
    for harf in cumle:
        if 65 <= ord(harf) <= 90:
            sayi += 1
    return sayi




def Tr2Eng(cumle):
    ncumle = ""
    for i in cumle:
        if(i == "ç"):
            ncumle += "c"
        elif(i == "ğ"):
            ncumle += "g"
        elif(i == "ı"):
            ncumle += "i"                    
        elif(i == "ö"):
            ncumle += "o"
        elif(i == "ş"):
            ncumle += "s"
        elif(i == "ü"):
            ncumle += "u"
        elif(i == "Ç"):
            ncumle += "C"
        elif(i == "Ğ"):
            ncumle += "G"
        elif(i == "İ"):
            ncumle += "I"
        elif(i == "Ö"):
            ncumle += "O"
        elif(i == "Ş"):
            ncumle += "S"
        elif(i == "Ü"):
            ncumle += "U"
        else:
            ncumle += i
    return ncumle
print(Tr2Eng("üöçğş"))





def BasamakDegeri(Liste):
    toplam = 0
    for sayi in Liste:
        sayac = 0
        for i in str(sayi):              
            sayac += 1
        toplam += sayac
    return toplam

print(BasamakDegeri([1,10,100]))
