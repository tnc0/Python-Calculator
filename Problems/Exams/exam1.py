def tirnak(kelimem = "adad", cumle = "adad dad abc"):
    sayac = 0
    kelime = ""
    for harf in cumle:
        if(harf != " "):
             kelime+= harf
        else:
            if(kelime == kelimem):
                cumle[sayac] = f'"{kelime}"'
                return cumle
            kelime = ""
            sayac += 1
        


################ cumledeki kelimeleri bulmayı öğrenmem gerekiyor.

"""
#GPT
# Kullanıcıdan metni ve aranan kelimeyi al
metin = input("Bir metin girin: ")
aranan_kelime = input("Tırnak eklemek istediğiniz kelimeyi girin: ")

# Yeni metni oluştur
yeni_metin = ""
kelime_baslangic = 0

for i in range(len(metin)):
    if metin[i:i+len(aranan_kelime)] == aranan_kelime:
        yeni_metin += '"' + aranan_kelime + '"'
        kelime_baslangic = i + len(aranan_kelime)
        break
    else:
        yeni_metin += metin[i]

for i in range(kelime_baslangic, len(metin)):
    if metin[i] == ' ':
        yeni_metin += ' '  # Boşlukları geç
    else:
        yeni_metin += metin[i]
        if i == len(metin) - 1:
            yeni_metin += '"'  # Cümlenin sonunda ise tırnak ekle

# Sonucu ekrana yazdır


"""





#yazıdaki bir karakteri sil.
#tamamdır

def karakter_sil(harfim = "d", cumle = "adad dad abc"):
    
    yenicumle = ""
    for harf in cumle:
        if(harf != harfim):
            yenicumle += harf
        else:
            continue
    return yenicumle



#yazıdaki bir kelimeyi sil.
#tamam

def kelime_sil(kelimem = "abc", cumle = "adad dad abc"):
    yenicumle = ""
    kelime = ""
    for harf in cumle + " ":
        if(harf != " "):
            kelime += harf
        else:
            if(kelime != kelimem):
                yenicumle += kelime + " "
            kelime = ""
    return yenicumle




def tirnak(kelimem = "adad", cumle = "adad dad abc"):
    yenicumle = ""
    kelime = ""
    for harf in cumle + " ":
        if(harf != " "):
             kelime+= harf
        else:
            if(kelime == kelimem):
                yenicumle += f'"{kelime}"'    
                kelime = ""
            if(kelime != kelimem):
                yenicumle += kelime + " "
                kelime = ""
    return yenicumle


