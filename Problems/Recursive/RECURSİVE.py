#n! = n*(n-1)!

def facto(n):
    if(n == 0):
        return 1 #bir fonksiyonda return edilirse o fonksiyondan çıkılır.
    return facto(n-1)*n

print(facto(0))

#x = (x-1)+(x-2)

def fibo(x):

    if(x == 0 or x == 1):
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(5))
