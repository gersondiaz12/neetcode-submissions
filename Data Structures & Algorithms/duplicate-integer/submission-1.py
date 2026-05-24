class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        prev_index = 0
        result = False

        for num in nums[1:]:
            if nums[prev_index] == num:
                result = True
                break
            else:
                prev_index+= 1
        
        return result
        