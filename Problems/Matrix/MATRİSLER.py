"""
"""
# 2 matrisin toplamını yazdırdım.


def matris_toplama(matris_a, matris_b):
    
    sonuc_matris = [[0 for _ in range(len(matris_a))] for _ in range(len(matris_a))]

    for a1 in range(len(matris_a)):
        for a2 in range(len(matris_a)):
            print(matris_a[a1][a2],end=" ")
        print()
    print()
    for b1 in range(len(matris_b)):
        for b2 in range(len(matris_b)):
            print(matris_b[b1][b2],end=" ")
        print()
    print() 
    for i in range(len(matris_a)):
        for j in range(len(matris_a)):
            sonuc_matris[i][j] = matris_a[i][j] + matris_b[i][j]
            print(sonuc_matris[i][j],end=" ")
        print()
    return "tamamlandi"


matris_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matris_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

sonuc_matris = matris_toplama(matris_a, matris_b)

print(sonuc_matris)

#matristeki en büyük değeri buldum.

matris = [[1,2],[4,3]]
maks = matris[0][0]
for i in range(len(matris)):
    for j in range(len(matris)):
        if(matris[i][j] > maks):
            maks = matris[i][j]

print(maks)


# bir matrisin izin (diyagonal) toplamını buldum.
matris1 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

if(len(matris1[0]) == len(matris1)):
    toplam = 0
    x = 0
    for i in range(len(matris1)):
        toplam += matris1[i][x]
        x +=1
    print(toplam)
else:
    print("kare matris girmen lazım")

#Verilen sayıyı matrisin k. indeksine yerleştirdim.

matris2 = [[1,2],
           [3,4],
           [7,8],
           [5,6]]

s = 10

satir = 3
sutun = 0

for i in range(len(matris2)):
    for j in range(len(matris2)):
        if (i == satir and j == sutun):
            matris2[i][j] = s
            print(matris2)


#  matrisin transpozunu aldım.

""" istediğim şey
[[1,4],
 [2,5],
 [3,6]] 
"""

matris3 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
c = [[0 for _ in range(3)] for _ in range(3)]
print(c)
for i in range(len(matris3)):
    for j in range(len(matris3)):
        c[i][j] = matris3[j][i]
print(c)
        





def matris_toplama(matris_a, matris_b):
    sonuc_matris = [[0 for _ in range(len(matris_a))]for _ in range(len(matris_a))]
    for i in range(len(matris_a)):
        for j in range(len(matris_a)):
            print(matris_a[i][j],end=" ")
        print()
    print()
    

    for i in range(len(matris_b)):
        for j in range(len(matris_b)):
            print(matris_b[i][j], end=" ")
        print()
    print()

    for i in range(len(matris_a)):
        for j in range(len(matris_a)):
            sonuc_matris[i][j] = matris_a[i][j] + matris_b[i][j]
            print(sonuc_matris[i][j],end=" ")
        print()
    return "tamamlandı"

matris_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matris_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

sonuc_matris = matris_toplama(matris_a, matris_b)

print(sonuc_matris)
