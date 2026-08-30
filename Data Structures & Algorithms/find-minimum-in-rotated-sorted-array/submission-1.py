class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = max(nums)

        if nums[r] > nums[l]: return nums[l] 

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[0]:
                l = m + 1
            elif nums[m] <= nums[-1]:
                r = m - 1
        
        return res

# what i learned
    # since we rotated the array, we have two portion of the array that are sorted
    # so when evaluating the middle ptr, which portion are we in?
    # if we are in the left portion, we want to look at the right portion for the min value
    # to check for this, we determine if middle ptr is >= the first index
        # if it's true: we are still in the left portion
        # if it's false: we are in the right portion 