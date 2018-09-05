n, m = map(int, input().split())
lyst = [i for i in range(1, n + 1)]
for i in range(m):
    num = int(input())
    lyst.remove(num)
    lyst.insert(0, num)
for el in lyst:
    print(el)


"""
5 3
4
2
5
"""
