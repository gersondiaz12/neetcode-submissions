class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res, sizes = "", []
        for s in strs:
            sizes.append(len(s))
        
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'

        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res, sizes, i = [], [], 0
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1

        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        
        return res
