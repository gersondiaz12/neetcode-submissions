class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {} # char : count
        res, l = 0, 0

        for r in range(len(s)):
            myMap[s[r]] = 1 + myMap.get(s[r], 0)
            
            if (r - l + 1) - max(myMap.values()) > k:
                myMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
