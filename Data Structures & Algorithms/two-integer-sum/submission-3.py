class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {} # value : index

        for i, n in enumerate(nums): # value, index
            diff = target - n
            if diff in check:
                return [check[diff], i]
            
            check[n] = i
        
        return
