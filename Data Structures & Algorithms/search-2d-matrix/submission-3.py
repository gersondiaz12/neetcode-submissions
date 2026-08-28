class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search #1
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break # we found our desired row

        # its possible if we did not break out, we figured out a condition where the top and bottom pointers are invalid, we crossed out every row in the matrix

        if not (top <= bot): # none of the rows contain the target value
            return False
        
        # binary search #2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False
        



# the second property of the input matrix is important: the first int of each row is greater than the last int in the previous row
# we can implement a double binary search
# binary search #1: each row to find the row of our target value
# binary search #2: each value withing our sorted row, to find our target value