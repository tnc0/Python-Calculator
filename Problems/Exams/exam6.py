def fonksiyonum(kelimeler,hedef):

    control = 0

    if(hedef[0] == hedef[1] and hedef[1] != hedef[2] and hedef[0] != hedef[2]):#sondaki farklı
        control = 1
    if(hedef[1] == hedef[2] and hedef[0] != hedef[1] and hedef[0] != hedef[2]):#baştaki farklı
        control = 2
    if(hedef[0] == hedef[2] and hedef[0] != hedef[1] and hedef[1] != hedef[2]):#ortadaki farklı
        control = 3
    if(hedef[0] != hedef[1] and hedef[1] != hedef[2] and hedef[0] != hedef[2]):#hepsi farklı
        control = 4
    if(hedef[0] == hedef[1] and hedef[1] == hedef[2] and hedef[0] == hedef[2]):#hepsi eşit
        control = 5


    for kelime in kelimeler:
        if(control == 1):
            if(kelime[0] == kelime[1] and kelime[1] != kelime[2] and kelime[0] != kelime[2]):
                print(kelime)
        if(control == 2):
            if(kelime[1] == kelime[2] and kelime[0] != kelime[1] and kelime[0] != kelime[2]):
                print(kelime)
        if(control == 3):
            if(kelime[0] == kelime[2] and kelime[0] != kelime[1] and kelime[1] != kelime[2]):
                print(kelime)
        if(control == 4):
            if(kelime[0] != kelime[1] and kelime[1] != kelime[2] and kelime[0] != kelime[2]):
                print(kelime)
        if(control == 5):
            if(kelime[0] == kelime[1] and kelime[1] == kelime[2] and kelime[0] == kelime[2]):
                print(kelime)

fonksiyonum(["abc","abb","aab","aba","aaa"],"pyt")