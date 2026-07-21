class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            res = max(res, r - l + 1)
        
        return res


# what i didn't understand:
    # why doesnt a two-pointer sliding window solution work?
# what i learned:
    # for sliding window, you need to use a set to keep track of all characters inside the string, not just the beginning character(left pointer)
    # 

        