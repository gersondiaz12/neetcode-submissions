class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if (cell in rows[r] or 
                    cell in cols[c] or 
                    cell in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(cell)
                rows[r].add(cell)
                squares[(r // 3, c // 3)].add(cell)
        return True
                