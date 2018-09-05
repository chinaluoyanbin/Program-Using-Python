"""
链接：https://www.nowcoder.com/questionTerminal/6acc6504df67406c98a75f5575e4b94a?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。
"""


class paint(object):
    def __init__(self, n, m, target):
        self.n = n
        self.m = m
        self.target = target
        self.count = 0

    def dfs_Y(self, x, y):
        if 0 <= x < n and 0 <= y < m and (self.target[x][y] == 'Y'
                                          or self.target[x][y] == 'G'):
            if self.target[x][y] == 'G':
                self.target[x][y] = 'B'
            else:
                self.target[x][y] = 'X'
            self.dfs_Y(x - 1, y - 1)
            self.dfs_Y(x + 1, y + 1)

    def dfs_B(self, x, y):
        if 0 <= x < n and 0 <= y < m and (self.target[x][y] == 'B'
                                          or self.target[x][y] == 'G'):
            if self.target[x][y] == 'G':
                self.target[x][y] = 'Y'
            else:
                self.target[x][y] = 'X'
            self.dfs_B(x - 1, y + 1)
            self.dfs_B(x + 1, y - 1)

    def min_operation_count(self):
        for i in range(n):
            for j in range(m):
                if self.target[i][j] == 'Y':
                    self.dfs_Y(i, j)
                    self.count += 1
                elif self.target[i][j] == 'B':
                    self.dfs_B(i, j)
                    self.count += 1
                elif self.target[i][j] == 'G':
                    self.dfs_Y(i, j)
                    self.dfs_B(i, j)
                    self.count += 2
        return self.count

while True:
    try:
        n, m = map(int, input().split())
        target = []
        for i in range(n):
            target.append(list(input()))
        painting = paint(n, m, target)
        print(painting.min_operation_count())
    except:
        break
