class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashy:
                return [hashy[diff], i]
            
            hashy[n] = i
            