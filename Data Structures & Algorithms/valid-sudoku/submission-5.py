class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue
                
                if cell not in rows[r] and cell not in cols[c] and cell not in boxes[(r // 3, c // 3)]:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[(r // 3, c // 3)].add(cell)
                else:
                    return False
        
        return True