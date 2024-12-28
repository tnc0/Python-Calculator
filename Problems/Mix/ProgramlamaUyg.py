"""
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

k = int(input("kaç defa kaydirilsin\n"))
print(l)

for i in range(k):
    l = [l[-1]] + l[:-1]
    print(l)
    """

"""
l1=[1,1,2,3,5,8,13,21,34,55,89]
l2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
l3=[]
for i in l1:
    for g in l2:
        if(i == g):
            l3.append(i)
print(l3)

"""