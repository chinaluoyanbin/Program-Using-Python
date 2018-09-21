class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [[-10000000] * n for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(n):
                if j + i <= n:
                    dp[i][j] = max(dp[i - 1][j], sum(nums[j: j + i]))
                else:
                    dp[i][j] = dp[i - 1][j]
        return max(dp[n])
        
ins = Solution()
s = [-2,1,-3,4,-1,2,1,-5,4]
print(ins.maxSubArray(s))

