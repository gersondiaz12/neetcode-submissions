class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l] # this will never be negative, because we update the max BEFORE subtracting
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res
            




# what i did not understand:
    # how do we calculate the amount of water trapped in between two tall structures?
    # do we use the same two pointer approach from 'containter with most water'?
    # for each iteration, how do we find the highest left and right boundary?

# what i learned:
    # for each index, calculate the min(l, r) and subtract by current height. The result will be how much water can be trapped at that space.
    # use two pointers, keep track of MaxL and MaxR everytime you update pointers.
    # shift the pointer that has the smaller max value each time
    # 

        