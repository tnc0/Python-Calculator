import random
def matrisi_ekrana_yaz(matris,ad): #function
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()
    print()


satir = int(input("satır:"))
sutun = int(input("sütun:"))


matris1 = [[round(10*random.random()) for _ in range(satir)] for _ in range(sutun)]     # arg_1

matris2 = [[round(10*random.random()) for _ in range(satir)] for _ in range(sutun)]     # arg_2

toplammatris = [[0 for _ in range(satir)] for _ in range(sutun)]     # total matrisutun

for i in range(sutun):
    for j in range(satir):
        toplammatris[i][j] = matris1[i][j] + matris2[i][j]     # total

matrisi_ekrana_yaz(matris1,'A')
matrisi_ekrana_yaz(matris2,'B')
matrisi_ekrana_yaz(toplammatris,'C')


