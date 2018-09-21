"""
测试用例：
4 3
1 2
1 3
3 4
"""


class Solution(object):
    def __init__(self, N, m, edges):
        self.N = N
        self.m = m
        self.edges = edges
        self.neighbors = {}
        self.graph_initial()

    def graph_initial(self):
        for i in range(1, self.N + 1):
            self.neighbors[i] = []
        for edge in self.edges:
            u, v = edge
            if u not in self.neighbors[v]:
                self.neighbors[v].append(u)
            if v not in self.neighbors[u]:
                self.neighbors[u].append(v)
    
    def breadth_first_search(self):
        from collections import deque
        begin = 1
        end = self.N
        if begin == end:
            return 1
        
        visited = set([begin])  # 已经便利过的节点
        q = deque([1])  # 新建一个队列
        dis = 0  # 计数
        while q:
            dis += 1
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                for neighbor in self.neighbors[node]:
                    if neighbor == end:
                        return dis
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        return -1


N, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(tuple(map(int, input().split())))
ins = Solution(N, m, edges)
print(ins.breadth_first_search())
