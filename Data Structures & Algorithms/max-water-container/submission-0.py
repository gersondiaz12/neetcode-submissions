class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            
            if heights[l] < heights[r]: # shift left pointer to the right, because we want to maximize both heights
                l += 1
            else:
                # shift right pointer to the left, because we want to maximize both heights
                # if height[l] == height[r], it doesn't matter which pointer we shift, so to condense code, we shift right in this case
                r -= 1
        
        return res

             
        