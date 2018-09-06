"""
5 3
3 1 2 3
3 3 4 2
3 3 5 4
"""


class Solution(object):
    def __init__(self, n):
        self.neighbors = {}
        self.visited = {}
        self.routes = {}
        self.current_route = -1
        self.count = 0
        self.n = n
        self.res = []

    def add_nodes(self):
        for i in range(1, self.n + 1):
            self.add_node(i)

    def add_node(self, node):
        if node not in self.nodes():
            self.neighbors[node] = []

    def nodes(self):
        return self.neighbors.keys()

    def visited_initial(self):
        for node in self.nodes():
            self.visited[node] = False

    def add_edge(self, edge, number):
        self.routes[edge] = number
        node, neighbor = edge
        if neighbor not in self.neighbors[node]:
            self.neighbors[node].append(neighbor)

    def breadth_first_search(self, root=1):
        queue = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)

                self.visited[node] = True
                temp = self.count
                for n in self.neighbors[node]:
                    self.count = temp
                    if not self.visited[n]:
                        queue.append(n)
                        if self.current_route != self.routes[(node, n)]:
                            self.count += 1
                        if n == self.n:
                            self.res.append(self.count)
                        else:
                            bfs()

        for n in self.neighbors[root]:
            self.visited_initial()
            self.visited[n] = True
            self.count = 0
            self.current_route = self.routes[(root, n)]
            self.count += 1
            queue.append(n)
            bfs()

        return min(self.res)


n, m = map(int, input().split())
ins = Solution(n)
ins.add_nodes()
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp) - 1):
        ins.add_edge((temp[j], temp[j + 1]), i)
print(ins.breadth_first_search())
