import random

def matrisiyazdir(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j],end=" ")
        print()

b = 2

A = [[round(10*random.random()) for _ in range(b)]for _ in range(b)]

matrisiyazdir(A,"A")

satirtoplam = []

for i in range(b):
    top = 0
    for j in range(b):
        top += A[i][j]
    satirtoplam.append(top)
print("satir toplam",satirtoplam)

sutuntoplam = []

for j in range(b):
    top = 0
    for i in range(b):
        top += A[i][j]
    sutuntoplam.append(top)
print("sutun toplam",sutuntoplam)