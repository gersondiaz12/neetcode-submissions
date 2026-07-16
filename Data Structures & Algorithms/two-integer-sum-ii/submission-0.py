class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

#example:
#[1, 3, 4, 5, 7, 11] target = 9
#output:
#[4, 5]

# use two pointers. add each pointer together to see if it's greater
    # than or less than the target
# increment the left pointer or decrement the right pointer, based on 
    # whatever makes the sum less than/greater than before