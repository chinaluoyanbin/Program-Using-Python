class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = -1
        freq = [0] * 256
        res = 0
        while left < len(s):
            if right + 1 < len(s) and freq[ord(s[right + 1])] == 0:
                freq[ord(s[right + 1])] += 1
                right += 1
            else:
                freq[ord(s[left])] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

ins = Solution()
print(ins.lengthOfLongestSubstring("bbbbb"))
