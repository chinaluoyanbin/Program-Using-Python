import math


class eatChocolates(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def sum_of_chocolates(self, num):
        s = 0
        for i in range(self.n):
            s += num
            num = math.ceil(num / 2)
        return s

    def max_chocolates_first_day(self):
        if self.n == 1:
            return self.m
        low = 1
        high = self.m
        while low < high:
            mid = math.ceil((low + high) / 2)
            if 


n, m = map(int, input().split())
smallQ = eatChocolates(n, m)
