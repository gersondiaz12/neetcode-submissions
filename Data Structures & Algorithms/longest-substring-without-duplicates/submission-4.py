class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            
            count.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res
