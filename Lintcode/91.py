class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        max_int = 2147483647
        n = len(A)
        dp = [[max_int for i in range(101)] for i in range(n + 1)]  # 新建dp矩阵 (n+1)x101
        for i in range(101):
            dp[0][i] = 0
        for i in range(1, n + 1):
            for j in range(1, 101):
                for k in range(1, 101):
                    if abs(j - k) <= target:
                        dp[i][j] = min(dp[i - 1][k] + abs(A[i - 1] - j), dp[i][j])
        return min(dp[n])
