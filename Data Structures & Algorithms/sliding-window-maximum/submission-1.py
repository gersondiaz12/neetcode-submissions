class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0
        q = collections.deque() # index

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove the left value from the window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        

# what i didn't know:
    # how to append values in between the left and right pointer of the window for comparison

# what i learned:
    # if we use a window and have a value that's greater than the previous values, than we can eliminate those values from our window
    # when using a deque, values are always in decreasing order
    # once we have a greater value, pop the top of the deque until it's the new smallest value; add the value to the deque
    # if we want the max value, we fetch the leftmost value of our deque, since it's in decreasing order
    # 
