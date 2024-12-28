def spiralMatrix(m,n,num):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    print(matrix)
    
    a = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = num[a]
            a += 1
    print(matrix)

spiralMatrix(3,5,[3,0,2,6,8,1,7,9,4,2,5,5,0])