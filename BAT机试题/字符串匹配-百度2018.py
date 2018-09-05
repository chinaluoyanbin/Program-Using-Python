"""
::算例1::
    :输入:
        00010001
        ??
    :输出:
        3
"""


class StringMatch(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.count = 0

    def matching(self, lyst):
        if '?' in lyst:
            index = lyst.index('?')
            lyst[index] = '0'
            self.matching(lyst)
            lyst[index] = '?'
            lyst[index] = '1'
            self.matching(lyst)
            lyst[index] = '?'
        else:
            if ''.join(lyst) in self.a:
                self.count += 1

    def begin(self):
        lyst = list(self.b)
        self.matching(lyst)
        return self.count


while True:
    try:
        a = input()
        b = input()
        niuniu = StringMatch(a, b)
        print(niuniu.begin())
    except:
        break
