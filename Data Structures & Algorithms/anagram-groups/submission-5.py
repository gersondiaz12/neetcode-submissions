class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # automatically set 0's

        for s in strs:
            count = [0] * 26 # array

            for c in s:
                count[ord('a') - ord(c)] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())