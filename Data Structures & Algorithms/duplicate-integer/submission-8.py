class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {} # num : count

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > 1:
                return True
        
        return False