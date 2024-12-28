# listede en çok tekrar eden sayı #
# listeyi küçükten büyüğe sırala
# büyük harfleri başa al küçük harfleri sona al
# bir sayının bütün çarpanlarının kendisi ile çarpımı
# matris toplamı #

# matris toplamı #
#TAMAMDIR
def matristoplama(matris1,matris2):
    sonucmatris = [[0 for _ in range(len(matris1))]for _ in range(len(matris1))]

    for i in range(len(sonucmatris)):
        for j in range(len(sonucmatris)):
            sonucmatris[i][j] = matris1[i][j] + matris2[i][j]

    return sonucmatris
matris1 = [[1,2],
           [2,1]]
matris2 = [[1,2],
           [2,1]]



# listede en çok tekrar eden sayı
#TAMAMDIR
def encoktekrar(liste):
    maxtekrarsayisi = 0
    encoktekraredensayi = None

    for i in liste:
        tekrar = 0
        for j in liste:
            if(i == j):
                tekrar += 1
        if(tekrar > maxtekrarsayisi):
            maxtekrarsayisi = tekrar
            encoktekraredensayi = i
    return f"en çok tekrar eden sayı:{encoktekraredensayi}, tekrar sayısı:{maxtekrarsayisi}"

ornek = [1,1,1,2,3,3]


# EN COK TEKRAR EDEN SAYIYI SİL.
#TAMAMDIR
def encoktekrar(liste):
    yeniliste = []
    maxtekrarsayisi = 0
    encoktekraredensayi = None

    for i in liste:
        tekrar = 0
        for j in liste:
            if(i == j):
                tekrar += 1
        if(tekrar > maxtekrarsayisi):
            maxtekrarsayisi = tekrar
            encoktekraredensayi = i
    for i in liste:
        if(i != encoktekraredensayi):
            yeniliste.append(i)
    return yeniliste
ornek = [1,1,1,2,3,3]






# listede en çok tekrar eden sayı

def en_cok_tekrar_eden_sayi(liste):
    max_tekrar_sayisi = 0
    en_cok_tekrar_eden = None

    for i in liste:
        tekrar_sayisi = 0
        for j in liste:
            if i == j:
                tekrar_sayisi += 1

        if tekrar_sayisi > max_tekrar_sayisi:
            max_tekrar_sayisi = tekrar_sayisi
            en_cok_tekrar_eden = i

    return en_cok_tekrar_eden, max_tekrar_sayisi

# Örnek bir liste
ornek_liste = [1, 2, 3, 4, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Fonksiyonu kullanarak en çok tekrar eden sayıyı bulma
en_cok_tekrar_eden, tekrar_sayisi = en_cok_tekrar_eden_sayi(ornek_liste)

# print(f"En çok tekrar eden sayı: {en_cok_tekrar_eden}")
# print(f"Tekrar sayısı: {tekrar_sayisi}")





# listeyi küçükten büyüğe sırala
#DAHA YAPILMADI
def listem(liste = [2,4,3,1]):
    for i in range(len(liste)):
        for j in range(0, (len(liste))-i-1):
            if(liste[j] > liste[j+1]):
                liste[j], liste[j+1] = liste[j+1], liste[j]
            
    return liste

print(listem())


