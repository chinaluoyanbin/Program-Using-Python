class Solution(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.visited = []

    def function(self):
        for el in self.b:
            if el not in self.visited:
                self.visited.append(el)
                if el not in self.a:
                    return 0
                cnt_a = self.a.count(el)
                cnt_b = self.b.count(el)
                if cnt_a < cnt_b:
                    return 0
        return 1

while True:
    try:
        a = input()
        b = input()
        ins = Solution(a, b)
        print(ins.function())
    except:
        break
