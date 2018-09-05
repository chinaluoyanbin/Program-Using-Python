"""
5 3
3 1 2 3
3 3 4 2
3 3 5 4
"""


class Solution(object):
    def __init__(self, n, starts, remains):
        self.n = n
        self.starts = starts
        self.remains = remains
        self.cost = 100001
        self.count = 0
        self.visited = []

    def bfs(self, x):
        if x == self.n:
            if self.count < self.cost:
                self.cost = self.count
        else:
            for remain in self.remains:
                if remain[0] == x and remain not in self.visited:
                    self.visited.append(remain)
                    self.count += 1
                    for el in remain[1:]:
                        self.bfs(el)

    def begin(self):
        for start in self.starts:
            self.count = 1
            self.visited = []
            for el in start[1:]:
                self.bfs(el)
        return self.cost


n, m = map(int, input().split())
starts = []
remains = []
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[1] == 1:
        starts.append(temp[1:])
    else:
        remains.append(temp[1:])
instance = Solution(n, starts, remains)
print(instance.begin())
