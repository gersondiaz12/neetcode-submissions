class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value : count
        freq = [[] for i in range(len(nums) + 1)]
        # 0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # 1 : 1, # 2 : 2, #3 : 3
        
        for v, c in count.items():
            freq[c].append(v)
        # 0: [], 1: [1], 2: [2], 3: [3], 4: [], 5: [], 6: []
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res