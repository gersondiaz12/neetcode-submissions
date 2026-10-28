class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # pick any num in array as default
        l, r = 0, len(nums) - 1

        while l <= r:
            # check if the array is already sorted, then our result is the left-most value
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r)  // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # are we in the left-sorted portion? (greater vals) If so, we search right
                l = m + 1
            else: # are we in the right-sorted portion? (lower vals) If so, we search left
                r = m - 1
    
        return res