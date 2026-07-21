class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # the '0' represents the default value if the character doesn't exist

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

# what i didn't know:
    # how do i want all characters in a window to match the most common character in that window?

# what did i learn:
    # use a hashmap to count every occurance of each character
    # take the length of the window, and subtract it by the count of the most frequent character
        # this represents the amount of characters that needs to be replaced
        # make sure that this value is not greater than k
    # use sliding window technique with two pointers 
    # once we reach an invalid window, shrink the size of the window until its valid by shifting the left pointer to the right
        # decrement the count of characters while moving the pointer