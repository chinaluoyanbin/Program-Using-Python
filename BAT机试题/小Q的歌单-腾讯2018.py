"""腾讯2018秋招笔试"""

mod = 1000000007


def init():
    """杨辉三角形"""
    c = [[0 for i in range(101)] for i in range(101)]
    c[0][0] = 1
    for i in range(1, 101):
        c[i][0] = 1
        for j in range(1, 101):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
    return c


while True:
    try:
        k = int(input())
        a, x, b, y = map(int, input().split())
        count = 0
        c = init()
        for i in range(0, x + 1):
            if i * a <= k and (k - i * a) % b == 0 and (k - i * a) / b <= y:
                count = (count + (c[x][i] * c[y][(k - i * a) // b]) % mod) % mod
        print(count)
    except:
        break
