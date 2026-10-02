class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashS, hashT = [0] * 26, [0] *26

        for c in s:
            hashS[ord(c) - ord('a')] += 1
        
        for c in t:
            hashT[ord(c) - ord('a')] += 1

        for k, v in enumerate(hashS):
            if v != hashT[k]:
                return False
        
        return True