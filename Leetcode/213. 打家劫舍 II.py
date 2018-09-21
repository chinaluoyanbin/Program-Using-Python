class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        res = dp[n - 2]
        dp[0], dp[1] = 0, nums[1]
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return max(dp[n - 1], res)


ins = Solution()
print(ins.rob([1, 2, 3, 1]))
