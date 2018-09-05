class Solution(object):
    def __init__(self, target):
        self.target = target

    def solving(self):
        if self.target == '':
            return ''
        left = ''
        right = ''
        count = 0
        for el in self.target:
            if el == ']':
                count -= 1
            else:
                count += 1
            if count < 0:
                left += '['
                count += 1
        while count > 0:
            right += ']'
            count -= 1
        return left + self.target + right


while True:
    try:
        s = input()
        solution = Solution(s)
        print(solution.solving())
    except:
        break
