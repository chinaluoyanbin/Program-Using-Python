class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + dp[i - 2]
                if s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        return max(dp)

if __name__ == '__main__':
    ins = Solution()
    s = "(()))())("
    print(ins.longestValidParentheses(s))
