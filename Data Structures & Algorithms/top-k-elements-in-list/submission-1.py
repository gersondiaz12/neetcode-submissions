class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}

        for num in nums:
            hashy[num] = 1 + hashy.get(num, 0)
        
        arr = []
        for num, cnt in hashy.items(): 
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res

        