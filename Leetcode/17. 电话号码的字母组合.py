class Solution:
    def __init__(self):
        self.num_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        self.visited = set()

        def dfs(idx, target):
            for el in self.num_letters[self.digits[idx]]:
                if idx == len(self.digits) - 1:
                    self.visited.add(target + el)
                else:
                    dfs(idx + 1, target + el)

        if len(self.digits) == 0:
            return []

        idx = 0
        for el in self.num_letters[self.digits[idx]]:
            if idx + 1 < len(self.digits):
                dfs(idx + 1, '' + el)
            else:
                self.visited.add('' + el)
        return sorted(list(self.visited))

ins = Solution()
print(ins.letterCombinations('23'))
