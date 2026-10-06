class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # list : list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                # [1, 0, 1, ..., 1] act
            res[tuple(count)].append(s)

        return list(res.values())            
