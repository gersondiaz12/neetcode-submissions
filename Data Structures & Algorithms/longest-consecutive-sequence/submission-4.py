class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mySet = set(nums)

        for n in nums:
            # check if its start of sequence
            if (n - 1) not in mySet:
                currLength = 1
                while (n + currLength) in mySet:
                    currLength += 1
                
                longest = max(longest, currLength)
        
        return longest
                    
