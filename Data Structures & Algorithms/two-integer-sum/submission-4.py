class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in count:
                return [count[diff], i]
            
            count[n] = i