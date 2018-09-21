class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '' and p == '*':
            return True
        
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0 and j > 0:
                    dp[i][j] |= dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] in ['*', '?'])
                if i > 0 and j > 0:
                    dp[i][j] |= dp[i - 1][j] and p[j - 1] == '*'
                if j > 0:
                    dp[i][j] |= dp[i][j - 1] and p[j - 1] == '*'
        return dp[n][m]
