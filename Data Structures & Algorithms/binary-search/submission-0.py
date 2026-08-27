class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1


# what I learned:
#   We use binary search algorithm
#   We use two pointers, one for left, and one for left
#   We take these two indexes and divide it by two, and ask if it's smaller or larger than the target (since the arr is sorted)