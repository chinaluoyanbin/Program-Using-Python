def dp(n, m):
    matrix = [[0] * 31 for i in range(31)] 
    matrix[0][0] = 1
    for i in range(1, m + 1):
        for j in range(n):
            if j == 0:
                matrix[i][j] = matrix[i - 1][n - 1] + matrix[i - 1][1]
            elif j == n - 1:
                matrix[i][j] = matrix[i - 1][n - 2] + matrix[i - 1][0]
            else:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j + 1]
    return matrix[m][0]

while True:
    try:
        n, m = map(int, input().split())
        print(dp(n, m))
    except:
        break
