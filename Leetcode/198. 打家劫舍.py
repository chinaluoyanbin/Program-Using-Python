class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        res = [-1] * n
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, n):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[n - 1]


ins = Solution()
print(ins.rob([1, 2, 3]))
