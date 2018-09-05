class Node(object):
    def __init__(self):
        self.S = []
        self.T = []


def solution(nodes):
    count = 0
    for node in nodes.values():
        if len(node.T) > len(node.S):
            count += 1
    return count


n, m = map(int, input().split())
nodes = {}
for i in range(1, n + 1):
    nodes[i] = Node()
for i in range(m):
    u, v = map(int, input().split())
    if u != v:
        if u not in nodes[v].T:
            nodes[v].T.append(u)
        if v not in nodes[u].S:
            nodes[u].S.append(v)
print(solution(nodes))


"""
4 3
2 1
3 1
1 4
"""
