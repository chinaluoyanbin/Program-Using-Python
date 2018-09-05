"""
4 3
3 2
1 2
1 4
3 2
4 2 1
"""


class Node(object):
    def __init__(self):
        # self.health = 0  # 0表示健康, 1表示中毒
        self.neighbors = []  # 该节点的邻居节点


class VirusInfection(object):
    def __init__(self, nodes, S, t):
        self.nodes = nodes
        self.S = set(S)
        self.t = t

    # def refresh(self):
    #     for node in self.nodes.values():
    #         node.health = 0

    def find_source(self):
        res = []
        for source in self.S:
            # self.refresh()  # 更新节点状态
            infected_nodes = set()  # 新建感染节点集合
            # self.nodes[source].health = 1
            infected_nodes.add(source)
            new_infected_nodes = set()
            new_infected_nodes.add(source)
            for day in range(1, self.t + 1):
                temp = set()
                for node in new_infected_nodes:
                    for neighbor in self.nodes[node].neighbors:
                        temp.add(neighbor)
                        infected_nodes.add(neighbor)
                new_infected_nodes = temp
            if infected_nodes == self.S:
                res.append(str(source))
        return res


# 读取输入数据
n, m = map(int, input().split())
e = []
for i in range(m):
    e.append(list(map(int, input().split())))
k, t = map(int, input().split())
S = list(map(int, input().split()))

# 新建n个节点
nodes = {}
for i in range(1, n + 1):
    nodes[i] = Node()

# 每个节点的邻居节点
for el in e:
    if el[0] != el[1]:
        if el[1] not in nodes[el[0]].neighbors:
            nodes[el[0]].neighbors.append(el[1])
        if el[0] not in nodes[el[1]].neighbors:
            nodes[el[1]].neighbors.append(el[0])

ins = VirusInfection(nodes, S, t)
print(' '.join(ins.find_source()))
