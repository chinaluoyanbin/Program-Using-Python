class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p = len(p)
        target_p = sorted(p)
        left = 0
        res = []
        while left < len(s):
            if left + len_p <= len(s) and sorted(s[left: left + len_p]) == target_p:
                res.append(left)
                left += 1
            else:
                left += 1
        return res
        
                
if __name__ == '__main__':
    ins = Solution()
    s = "baa"
    p = "aa"
    print(ins.findAnagrams(s, p))
