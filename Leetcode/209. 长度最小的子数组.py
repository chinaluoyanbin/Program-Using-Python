class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, -1
        sums = 0
        res = len(nums) + 1
        while left < len(nums):
            if right + 1 < len(nums) and sums < s:
                sums += nums[right + 1]
                right += 1
            else:
                sums -= nums[left]
                left += 1
            if sums >= s:
                res = min(res, right - left + 1)
        if res == len(nums) + 1:
            return 0
        return res
