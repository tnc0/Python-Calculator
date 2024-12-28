def terazi(A,B,C):

    liste = []

    a = (B+C-A)/3

    for i in range(100):
        if(i < a):
            liste.append(i)
    ilk = liste[0]
    son = liste[-1]
    return ilk,son
   
print(terazi(5,10,25))
