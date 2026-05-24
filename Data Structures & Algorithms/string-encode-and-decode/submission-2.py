class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        sizes, res = [], "" 
        for s in strs:
            sizes.append(len(s))
        for sz in sizes: # [5, 5]
            res += str(sz)
            res += ',' # "5,5,#"
        res += '#'
        for s in strs:
            res += s # "5,5,#HelloWorld"

        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1

        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        
        return res
