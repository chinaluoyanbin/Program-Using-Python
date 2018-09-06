def dp(N, m, goods):
    a = [[0] * (N + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(10, N + 1, 10):
            if goods[i - 1][2] == 0:
                if goods[i - 1][0] <= j:
                    a[i][j] = max(a[i - 1][j], a[i - 1][j - goods[i - 1][0]] + goods[i - 1][0] * goods[i - 1][1])
                else:
                    a[i][j] = a[i - 1][j]
            else:
                if (goods[i - 1][0] + goods[goods[i - 1][2] - 1][0]) <= j:
                    a[i][j] = max(a[i - 1][j], a[i - 1][j - goods[i - 1][0] - goods[goods[i - 1][2] - 1][0]] + goods[i - 1][0] * goods[i - 1][1] + goods[goods[i - 1][2] - 1][0] * goods[goods[i - 1][2] - 1][1])
                else:
                    a[i][j] = a[i - 1][j]
    return a[m][N // 10 * 10]

while True:
    try:
        N, m = map(int, input().split())
        goods = []
        for i in range(m):
            goods.append(list(map(int, input().split())))
        print(dp(N, m, goods))
    except:
        break
